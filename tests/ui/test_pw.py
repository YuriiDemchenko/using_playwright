import pytest
from playwright.sync_api import Page, expect


# This test checks if the title of the page is "DEMOQA"
@pytest.mark.pw
def test_has_title(page: Page):
    # Navigate to the page
    page.goto("https://demoqa.com/")
    # Expect the title of the page to be "DEMOQA"
    expect(page).to_have_title("DEMOQA")


# This test checks if the first element with class "card mt-4 top-card"
# can be clicked and the page header contains "Elements"
@pytest.mark.pw
def test_signup_page_title(page: Page):
    # Navigate to the page
    page.goto("https://demoqa.com/")
    # Query all elements with class "card mt-4 top-card"
    elements = page.query_selector_all(".card.mt-4.top-card")
    # Click the first element
    elements[0].click()
    # Locate the page header
    element_page_header = page.locator(".main-header")
    # Expect the page header to contain the text "Elements"
    expect(element_page_header).to_contain_text("Elements")
