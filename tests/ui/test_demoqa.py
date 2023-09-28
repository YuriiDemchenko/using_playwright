import pytest
from playwright.sync_api import Page, expect


# This test checks if the title of the page is "DEMOQA"
@pytest.mark.pw
def test_has_title(page: Page):
    # Expect the title of the page to be "DEMOQA"
    expect(page).to_have_title("DEMOQA")
