import pytest
import os
import requests
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def api_key():
    return os.getenv("STEAM_API_KEY")

@pytest.fixture
def api_url():
    return "https://api.steampowered.com"

@pytest.fixture
def steam_apps(api_url, api_key):
    response = requests.get(
        f"{api_url}/IStoreService/GetAppList/v1/",
        params={"key": api_key}
    )
    return response