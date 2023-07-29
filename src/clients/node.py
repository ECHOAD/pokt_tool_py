import logging
from os import environ
from random import randint
from ..utility import create_http_utility

from .models import NodeDetail

logger = logging.getLogger(__name__)

# Endpoints
ENDPOINTS = {
    "node": "/v1/query/node",
    "transaction": "/v1/query/tx"
}

client_hosts = environ.get('NODE_CLIENT_HOSTS').split(',')


def fetch_node_details(node_address):
    """Fetch node details from the Pokt Network."""
    response = None
    tries = 0

    while response is None and tries < len(client_hosts):
        try:

            node_http = create_http_utility(client_hosts[randint(0, len(client_hosts) - 1)])

            query = {
                'height': 0,
                'address': node_address,
            }

            response = node_http.post(ENDPOINTS.get("node"), data=query)

            if response.status_code == 400:
                return None

            response.raise_for_status()
        except Exception as e:
            print("Trying another client node host")
            logger.error(e)
            tries += 1

    if response is None:
        return None

    return NodeDetail(**response.json())


def get_detail_transaction_by_hash(tx_hash):
    """Get transactions details from TxHASH."""
    response = None
    tries = 0

    while response is None and tries < len(client_hosts):
        try:
            node_http = create_http_utility(client_hosts[randint(0, len(client_hosts) - 1)])

            query = {
                'hash': tx_hash,
                'prove': True
            }

            response = node_http.post(ENDPOINTS.get("transaction"), data=query)

            if response.status_code == 400:
                return None

            response.raise_for_status()
            return response.json()
        except Exception as e:
            print("Trying another client node host")
            logger.error(e)
            tries += 1
