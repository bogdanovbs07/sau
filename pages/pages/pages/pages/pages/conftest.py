import pytest
from playwright.sync_api import Page

@pytest.fixture
def base_url():
    return "https://www.saucedemo.com"

@pytest.fixture
def page(page: Page, base_url: str):
    page.goto(base_url)
    return page
