import requests

class SiteManagerAPI:
    def __init__(self, api_key: str, version: str = "v1", base_url: str = "https://api.ui.com/", verify_ssl: bool = True):
        self.api_key = api_key
        self.version = version
        self.base_url = base_url.rstrip('/')
        self.verify_ssl = verify_ssl  # <-- added toggle
        self.headers = {
            "X-API-KEY": f"{self.api_key}",
            "Accept": "application/json"
        }

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{self.version}/{endpoint.lstrip('/')}"
        response = requests.request(
            method,
            url,
            headers=self.headers,
            verify=self.verify_ssl,  
            **kwargs
        )
        response.raise_for_status()
        return response.json()

    # https://{host}/proxy/network/integration/{version}/sites
    def get_sites(self):
        return self._request("GET", "sites")

    # https://{host}/proxy/network/integration/{version}/sites/{site_id}/devices
    def get_unifi_devices(self, site_id):
        return self._request("GET", f"sites/{site_id}/devices")

    # https://{host}/proxy/network/integration/{version}/sites/{site_id}/clients
    def get_clients(self, site_id):
        return self._request("GET", f"sites/{site_id}/clients")
