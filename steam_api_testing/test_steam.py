import json

def test_get_steam_api_returns_200(steam_apps):
    assert steam_apps.status_code == 200

def test_get_steam_app_list(steam_apps):
    data = steam_apps.json()
    with open("steam_apps.json", "w") as f:
        json.dump(data, f, indent=2)
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