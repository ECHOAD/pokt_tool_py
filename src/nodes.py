import logging
import json
from .constants.http_status_codes import (HTTP_200_OK,
                                          HTTP_500_INTERNAL_SERVER_ERROR
                                          )

from flask import Blueprint, make_response, request

from .service import node
from .clients.encoders import NodeDetailEncoder, NodeTransactionEncoder, NodeRewardEncoder

nodes = Blueprint('nodes', __name__, url_prefix='/api/v1/nodes')
logger = logging.getLogger(__name__)


@nodes.get('<node_address>/details')
def get_node_details(node_address: str):
    """Get node details."""
    try:
        node_details = node.get_node_details_by_address(node_address)

        return make_response(json.dumps(node_details, cls=NodeDetailEncoder), HTTP_200_OK)
    except Exception as e:
        logger.error(e)
        return make_response(json.dumps({'message': 'Internal server error'}), HTTP_500_INTERNAL_SERVER_ERROR)


@nodes.get('<node_address>/rewards')
def get_node_rewards(node_address: str):
    """Get node details."""
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    start_date = request.args.get('start_date', type=str)
    end_date = request.args.get('end_date', type=str)
    order_by = request.args.get('order_by', type=str)

    try:
        node_rewards = node.get_rewards_from_node(node_address, start_date, end_date, limit=limit, offset=offset,
                                                  order_by=order_by)

        return make_response(json.dumps(node_rewards, cls=NodeRewardEncoder), HTTP_200_OK)
    except Exception as e:
        logger.error(e)
        return make_response(json.dumps({'message': 'Internal server error'}), HTTP_500_INTERNAL_SERVER_ERROR)


@nodes.get('<node_address>/transactions')
def get_all_transactions_by_address(node_address: str):
    """Get all nodes. Also with pagination"""
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    start_date = request.args.get('start_date', type=str)
    end_date = request.args.get('end_date', type=str)
    transaction_type = request.args.get('transaction_type', type=str)

    try:
        transactions = node.get_all_transactions_by_address(node_address, start_date, end_date, transaction_type, limit,
                                                            offset)

        return make_response(json.dumps(transactions, cls=NodeTransactionEncoder), HTTP_200_OK)
    except Exception as e:
        logger.error(e)
        return make_response(json.dumps({'message': 'Internal server error'}), HTTP_500_INTERNAL_SERVER_ERROR)


@nodes.get('/transactions')
def get_all_transactions():
    """Get all nodes. Also with pagination"""
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)

    try:
        transactions = node.get_all_transactions(page, limit)
        return make_response(json.dumps(transactions, cls=NodeTransactionEncoder), HTTP_200_OK)
    except Exception as e:
        logger.error(e)
        return make_response(json.dumps({'message': 'Internal server error'}), HTTP_500_INTERNAL_SERVER_ERROR)
