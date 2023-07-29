class NodeRewardDTO(object):
    """Class to handle pokt node rewards."""

    def __init__(self, node_address, tx_hash, block, amount_reward, chain, paid_at):
        self.node_address = node_address
        self.tx_hash = tx_hash
        self.block = block
        self.amount_reward = amount_reward
        self.chain = chain
        self.paid_at = paid_at

    def __repr__(self):
        return '<NodeReward: {}>'.format(self.node_address)

    def __str__(self):
        return 'NodeReward: {}'.format(self.node_address)
