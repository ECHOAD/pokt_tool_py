from ..constants.chains import AVAILABLE_POKT_CHAINS


def get_chain_detail_by_id(chain_id):
    """Get chain detail by id."""
    return AVAILABLE_POKT_CHAINS.get(chain_id, {
        "id": chain_id,
        "name": "Not Available",
    })


def get_chain_detail_by_name(chain_name):
    """Get chain detail by name."""
    for chain in AVAILABLE_POKT_CHAINS.values():
        if chain.get("name") == chain_name:
            return chain
    return None


def get_basic_chain_detail_by_id(chain_id):
    """Get basic chain detail by name."""
    chain = get_chain_detail_by_id(chain_id)

    return {
        "id": chain.get("id"),
        "name": chain.get("name", "N/A"),
    }
