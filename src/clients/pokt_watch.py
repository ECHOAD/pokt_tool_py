from datetime import datetime, timedelta
from dateutil.parser import parse as date_parse

from ..utility import create_http_utility
from .models import NodeTransaction

# Endpoints
ENDPOINTS = {
    "transaction": "/transaction",
}

http = create_http_utility("https://api.pokt.watch")

DATE_FORMAT = "%Y-%m-%d:%H:%M:%S"


def get_transactions(limit=50, offset=150):
    """
    Get all transactions from the Pokt Network.
    """
    response = http.get(ENDPOINTS["transaction"], {
        "order": "id.desc",
        "limit": limit,
        "offset": offset
    })

    return [NodeTransaction(**transaction) for transaction in response.json()]


def get_transactions_by_address(address: str, start_date=None, end_date=None, transaction_type=None, limit=50,
                                offset=0, order_by="id.desc"):
    """
    Get all transactions from address.
    """
    dynamic_query = []
    if not start_date or not end_date:
        now = datetime.now()
        if not start_date:
            start_date = (now - timedelta(days=30)).strftime(DATE_FORMAT)
        if not end_date:
            end_date = now.strftime(DATE_FORMAT)
    else:
        start_date = date_parse(start_date).strftime(DATE_FORMAT)
        end_date = date_parse(end_date).strftime(DATE_FORMAT)

    address_condition = "?or=(recipient.eq.{address}, signer.eq.{address})" \
        .format(address=address.upper())

    date_condition = "&and=(timestamp.gte.{start_date}, timestamp.lte.{end_date})".format(start_date=start_date,
                                                                                          end_date=end_date)
    limit_and_offset = "&limit={limit}&offset={offset}".format(limit=limit, offset=offset)

    dynamic_query.append(address_condition)
    dynamic_query.append(date_condition)
    dynamic_query.append(limit_and_offset)

    if transaction_type:
        transaction_condition = "&and=(msg_type.eq.{transaction_type})".format(transaction_type=transaction_type)
        dynamic_query.append(transaction_condition)

    order_by_condition = "&order={order_by}".format(order_by=order_by)
    dynamic_query.append(order_by_condition)

    query = "".join(dynamic_query)

    response = http.get(ENDPOINTS["transaction"] + query)

    return [NodeTransaction(**transaction) for transaction in response.json()]

