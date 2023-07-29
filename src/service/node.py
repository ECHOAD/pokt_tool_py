from ..clients import pokt_watch, node
from ..clients.models import NodeReward

from ..utility.chains import get_basic_chain_detail_by_id

POKT_TOKEN_VALUE = 1_000_000

def get_node_details_by_address(address: str):
    """
    Get node details from the Pokt Network.
    """
    return node.fetch_node_details(address)


def get_all_transactions(limit=50, offset=1500):
    """
    Get all transactions from the Pokt Network.
    """
    return pokt_watch.get_transactions(limit, offset)


def get_all_transactions_by_address(address: str, start_date, end_date, transaction_type, limit=50, offset=0):
    """
    Get all transactions from address.
    """
    return pokt_watch.get_transactions_by_address(address, start_date, end_date, transaction_type,
                                                  limit, offset)


def get_rewards_from_node(address: str, start_date=None, end_date=None, limit=50, offset=0, order_by="id.desc"):
    """Method to get rewards by node address """
    rewards_transaction = pokt_watch.get_transactions_by_address(address, start_date, end_date,
                                                                 transaction_type="claim", limit=limit,
                                                                 offset=offset, order_by=order_by)

    rewards = []

    for transaction_reward in rewards_transaction:
        transaction_claim = node.get_detail_transaction_by_hash(transaction_reward.hash)

        if transaction_claim:
            reward = NodeReward(
                transaction_claim["hash"],
                transaction_claim["height"],
                transaction_reward.timestamp,
                transaction_claim["stdTx"]["msg"]["type"],
                get_basic_chain_detail_by_id(transaction_claim["stdTx"]["msg"]["value"]["header"]["chain"]),
                transaction_claim["stdTx"]["msg"]["value"]["header"]["session_height"],
                transaction_claim["height"],
                transaction_claim["stdTx"]["msg"]["value"]["header"]["app_public_key"],
                transaction_reward.value / POKT_TOKEN_VALUE,
                True if transaction_reward.result_code == 0 else False
            )
            rewards.append(reward)

    return rewards
