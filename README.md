# QA Automation Portfolio

Personal QA automation portfolio built while transitioning from Manual QA to Automation QA.

**Stack:** Python 3.13 · pytest · requests · Playwright · python-dotenv

---

## Projects

### 1. API Base Tests — `pytest/base/`

Practice project using [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — a free public REST API.

**Covers:**
- GET requests and status code validation (200, 404)
- POST requests and response validation
- Field presence and type checking
- `conftest.py` fixtures for shared configuration (DRY principle)

**Run:**
```bash
cd pytest/base
pytest test_base.py -v
```

---

### 2. Steam API Tests — `pytest/steam_api_testing/`

Real-world API tests using the [Steam Web API](https://steamcommunity.com/dev).

**Covers:**
- App list validation (100k+ games)
- Required field and data type checks
- Game detail verification by `appid` (CS2, Elden Ring, Baldur's Gate 3)
- `pytest.mark.parametrize` for testing multiple games with one test function
- API key management via `.env` file (never committed to git)

**Run:**
```bash
cd pytest/steam_api_testing
pytest test_steam.py -v
```

> Requires a Steam API key in `.env`:
> ```
> STEAM_API_KEY=your_key_here
> ```

---

### 3. Steam UI Tests — `playwright/steam/`

End-to-end UI tests using [Playwright](https://playwright.dev/python/).

**Covers:**
- Search functionality validation
- Age verification gate — parametrized with positive and negative cases (underage users blocked)
- Role-based and attribute-based selectors

**Run:**
```bash
cd playwright/steam
pytest test_steam_ui.py -v --headed
```

---

## Setup

```bash
pip install requests pytest python-dotenv playwright pytest-playwright
playwright install
```

---

## Background

1 year of Manual QA experience at Keywords Studios (PowerWash Simulator 2 (credited), Netflix Puzzled (credited)).
This portfolio documents my self-study transition into automation testing.