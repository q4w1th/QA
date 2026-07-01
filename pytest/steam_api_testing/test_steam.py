import json
import requests
import pytest

def test_get_steam_api_returns_200(steam_apps):
    assert steam_apps.status_code == 200

def test_get_steam_app_list(steam_apps):
    data = steam_apps.json()
    json.dump(data, open("steam_apps.json", "w"), indent=2)
    assert "response" in data
    assert "apps" in data["response"]

def test_apps_have_required_fields(steam_apps):
    apps = steam_apps.json()["response"]["apps"]
    for app in apps[:50]:
        assert "appid" in app
        assert "name" in app
        assert "last_modified" in app
        assert isinstance(app["appid"], int)
        assert isinstance(app["name"], str)

@pytest.mark.parametrize("appid, expected_name", [
    (730,     "Counter-Strike 2"),
    (1245620, "ELDEN RING"),
    (1086940, "Baldur's Gate 3"),
])
def test_game_details(appid, expected_name):
    response = requests.get(
        "https://store.steampowered.com/api/appdetails",
        params={"appids": appid}
    )
    assert response.status_code == 200
    data = response.json()
    app = data[str(appid)]["data"]
    assert app["name"] == expected_name
    assert app["type"] == "game"