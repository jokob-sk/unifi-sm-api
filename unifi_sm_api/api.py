import requests

class SiteManagerAPI:
    def __init__(self, api_key: str, version: str ="v1", base_url: str = "https://api.ui.com/"):
        self.api_key = api_key
        self.version = version
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "X-API-KEY": f"{self.api_key}",
            "Accept": "application/json"
        }

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{self.version}/{endpoint.lstrip('/')}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_hosts(self):
        return self._request("GET", "hosts")

    def get_devices(self):
        return self._request("GET", "devices")


