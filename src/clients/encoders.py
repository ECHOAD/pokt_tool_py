import json
from .models import NodeDetail, NodeTransaction, NodeReward


class NodeDetailEncoder(json.JSONEncoder):
    """ Class to encode NodeDetail objects to JSON. """

    def default(self, obj: NodeDetail):
        if isinstance(obj, NodeDetail):
            return {
                "address": obj.address,
                "jailed": obj.jailed,
                "output_address": obj.output_address,
                "public_key": obj.public_key,
                "service_url": obj.service_url,
                "status": obj.status,
                "tokens": obj.tokens,
                "unstaking_time": obj.unstaking_time,
                "chains": obj.chains,
            }


class NodeRewardEncoder(json.JSONEncoder):
    """ Class to encode NodeReward objects to JSON. """

    def default(self, obj):
        if isinstance(obj, NodeReward):
            return {
                "hash": obj.hash,
                "height": obj.height,
                "time": obj.time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "type": obj.type,
                "chain": obj.chain,
                "session_height": obj.session_height,
                "expire_height": obj.expire_height,
                "app_pubkey": obj.app_pubkey,
                "pokt_per_relay": obj.pokt_per_relay,
                "is_confirmed": obj.is_confirmed,
            }
        return json.JSONEncoder.default(self, obj)


class NodeTransactionEncoder(json.JSONEncoder):
    """ Class to encode NodeTransaction objects to JSON. """

    def default(self, obj):
        if isinstance(obj, NodeTransaction):
            return {
                "id": obj.id,
                "height": obj.height,
                "hash": obj.hash,
                "index": obj.index,
                "result_code": obj.result_code,
                "signer": obj.signer,
                "recipient": obj.recipient,
                "msg_type": obj.msg_type.value,
                "fee": obj.fee,
                "memo": obj.memo,
                "value": obj.value,
                "timestamp": str(obj.timestamp)
            }
        return json.JSONEncoder.default(self, obj)
