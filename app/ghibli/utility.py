import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import logging

def fatal_code(e):
        return 400 <= e.response.status_code < 500

class HttpWrapper:
    """Adds logging and exponential backoff 
    on top of the requests library
    """

    def __init__(self, name):
        self.http_error_logger = logging.getLogger(name + '_http_logger')
        self.http_error_logger.addHandler(logging.StreamHandler())
        self.http_error_logger.setLevel(logging.ERROR)
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.client = requests.Session()
        self.client.mount("https://", adapter)
        self.client.mount("http://", adapter)

    def _get_logger(self):
        return self.http_error_logger

    def get_url(self, url, **kwargs):
        timeoutO = kwargs.get('timeout')
        timeout = timeoutO if timeoutO else 3.05
        return requests.get(url, timeout=timeout)