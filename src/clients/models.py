from datetime import datetime

from enum import Enum
from ..utility.chains import get_basic_chain_detail_by_id


class TransactionType(Enum):
    """Enum to handle transaction types."""
    CLAIM = 'claim'
    PROOF = 'proof'
    SEND = 'send'
    STAKE_VALIDATOR = 'stake_validator'
    BEGIN_UNSTAKE_VALIDATOR = 'begin_unstake_validator'
    UNJAIL_VALIDATOR = 'unjail_validator'

    @classmethod
    def get_type(cls, value):
        for type_of_transaction in cls:
            if type_of_transaction.value == value:
                return type_of_transaction
        raise ValueError('Invalid transaction type value: {}'.format(value))


class NodeDetail(object):
    """Class to handle pokt node detail."""

    def __init__(self, address, chains, jailed, output_address, public_key, service_url, status, tokens,
                 unstaking_time):
        self.address = address
        self.chains = [get_basic_chain_detail_by_id(chain) for chain in chains]
        self.jailed = jailed
        self.output_address = output_address
        self.public_key = public_key
        self.service_url = service_url
        self.status = status
        self.tokens = tokens
        self.unstaking_time = unstaking_time


class NodeTransaction(object):
    """Class to handle pokt node transactions."""

    def __init__(self, id, height, hash, index, result_code, signer, recipient, msg_type, fee, memo, value, timestamp):
        self.id = id
        self.height = height
        self.hash = hash
        self.index = index
        self.result_code = result_code
        self.signer = signer
        self.recipient = recipient
        self.msg_type = TransactionType.get_type(msg_type)
        self.fee = fee
        self.memo = memo
        self.value = value
        self.timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')


class NodeReward(object):
    """Class to handle pokt node rewards."""

    def __init__(self, hash, height, time, type, chain, session_height, expire_height, app_pubkey,
                 pokt_per_relay, is_confirmed):
        self.hash = hash
        self.height = height
        self.time = time
        self.type = type
        self.chain = chain
        self.session_height = session_height
        self.expire_height = expire_height
        self.app_pubkey = app_pubkey
        self.pokt_per_relay = pokt_per_relay
        self.is_confirmed = is_confirmed
