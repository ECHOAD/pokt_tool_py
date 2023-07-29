from .http import HttpUtility


def create_http_utility(base_url=None, headers=None):
    """
    Create an instance of the HttpService class.
    """
    return HttpUtility(base_url, headers)

