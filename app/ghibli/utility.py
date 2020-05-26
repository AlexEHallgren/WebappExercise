import logging
import http

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class HttpWrapper:
    """ Adds a logging and exponential backoff wrapper to requests."""
    def __init__(self, name):
        """ Initialise logging and HttpAdapter settings.

        Args:
            name (str): Used as a prefix for the logger instance.
        """
        http.client.HTTPConnection.debugLevel = 1
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=['HEAD', 'GET', 'OPTIONS']
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self._http = requests.Session()
        self._http.mount('https://', adapter)
        self._http.mount('http://', adapter)

    def get_url(self, url, **kwargs):
        """ Make a GET request.

        Args:
            url (str):The URL to make the request to.

        Keyword Arguments:
            timeout (float): Max time in seconds before a timeout occurs.

        Returns:
            requests.HttpResponse

        Raises:
            requests.HttpException: For HTTP errors.
        """
        timeoutO = kwargs.get('timeout')
        timeout = timeoutO if timeoutO else 3.05
        return self._http.get(url, timeout=timeout)
