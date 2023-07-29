import requests


default_header = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json, text/plain, */*',

}


class BaseHttpService(object):
    """Base class for HTTP services."""
    base_url = None
    headers = None

    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def get(self, url, params):
        pass

    def post(self, url, data):
        pass

    def put(self, url, data):
        pass

    def delete(self, url, params):
        pass

    def patch(self, url, data):
        pass

    def set_headers(self, headers):
        self.headers = headers

    def set_base_url(self, base_url):
        self.base_url = base_url


class HttpUtility(BaseHttpService):
    """Class to handle HTTP requests"""

    def __init__(self, base_url, headers=None):
        super().__init__(base_url, headers)
        if headers is None:
            super().set_headers(default_header)

    def get(self, url, params=None):
        response = requests.get(self.base_url + url, headers=self.headers, params=params)
        return response

    def post(self, url, data=None):
        response = requests.post(self.base_url + url, json=data, headers=self.headers)
        return response

    def put(self, url, data=None):
        response = requests.put(self.base_url + url, json=data, headers=self.headers)
        return response

    def delete(self, url, params=None):
        response = requests.delete(self.base_url + url, headers=self.headers, params=params)
        return response

    def patch(self, url, data=None):
        response = requests.patch(self.base_url + url, json=data, headers=self.headers)
        return response
