# QA Automation Portfolio

Personal QA automation learning project.

## Stack
- Python 3.13
- pytest
- requests

## Projects

### Base API Tests (`/base`)
Practice tests using JSONPlaceholder API.
- GET / POST requests
- Status code validation
- Field validation
- conftest.py fixtures

### Steam API Tests (`/steam_api_testing`)
Real-world API tests using Steam Web API.
- App list validation
- Game details verification
- parametrize for multiple games
- Environment variables for API key security

## How to run
```bash
pip install requests pytest python-dotenv
pytest steam_api_testing/test_steam.py -v
```