# UniFi Site Manager API Client

Python interface for interacting with UniFi’s Site Manager Integration API. Tested on selfhosted local instance only.

## 📦 Usage

```python
from unifi_sm_api.api import SiteManagerAPI

api = SiteManagerAPI(
    api_key="fakeApiKey1234567890",
    base_url="https://192.168.100.1/proxy/network/integration/",
    version="v1",
    verify_ssl=False
)

sites = api.get_sites()
devices = api.get_unifi_devices(site_id="site-id")
clients = api.get_clients(site_id="site-id")
```

---

## 📘 Endpoints Covered

- `/sites` — list available sites
- `/sites/{site_id}/devices` — list UniFi devices for a site
- `/sites/{site_id}/clients` — list connected clients

## 🔧 Requirements

- Python 3.8+
- `requests`
- `pytest` (for running tests)
- Local `.env` file with API credentials

---


## Testing

### 🌍 Environment Setup

Create a `.env` file in the project root with the following:

```env
API_KEY=fakeApiKey1234567890
BASE_URL=https://192.168.100.1/proxy/network/integration/
VERSION=v1
VERIFY_SSL=False
```
### 🧪 Running Tests

Make sure PYTHONPATH includes the project root, then run:

```bash
PYTHONPATH=.. pytest -s tests/test_api.py
```

