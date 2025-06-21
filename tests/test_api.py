import pytest
import json
import logging
from unifi_sm_api.api import SiteManagerAPI
from tests.config import API_KEY, BASE_URL, VERSION


logging.basicConfig(level=logging.INFO)

def test_init_hosts():
    api = SiteManagerAPI(api_key=API_KEY, version=VERSION, base_url=BASE_URL)
    result = api.get_hosts()

    print(json.dumps(result, indent=2))
    logging.info(json.dumps(result, indent=2))
    
def test_init_devices():
    api = SiteManagerAPI(api_key=API_KEY, version=VERSION, base_url=BASE_URL)
    result = api.get_devices()

    print(json.dumps(result, indent=2))
    logging.info(json.dumps(result, indent=2))
    