import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def demoqa(page: Page):
    page.goto("https://demoqa.com/")
    yield
