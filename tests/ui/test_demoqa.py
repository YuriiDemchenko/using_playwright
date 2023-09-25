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
def test_textbox(page: Page):
    data = {
        "userName": "John Doe",
        "userEmail": "john.d@fake.com",
        "currentAddress": "53 Palm st. Suite B",
        "permanentAddress": "Los Angeles, CA",
    }
    # Navigate to the page
    page.goto("https://demoqa.com/")
    # Query all elements with class "card mt-4 top-card" and click the first element
    page.query_selector_all(".card.mt-4.top-card")[0].click()

    page.get_by_text("Text Box").click()
    # Locate the page header
    item_page_header = page.locator(".main-header")
    # Expect the title of the page to be "Text Box"
    expect(item_page_header).to_contain_text("Text Box")

    username_label = page.locator("#userName-label")
    expect(username_label).to_contain_text("Full Name")

    email_label = page.locator("#userEmail-label")
    expect(email_label).to_contain_text("Email")

    current_address_label = page.locator("#currentAddress-label")
    expect(current_address_label).to_contain_text("Current Address")

    permanent_address_label = page.locator("#permanentAddress-label")
    expect(permanent_address_label).to_contain_text("Permanent Address")

    page.locator("#userName").fill(data["userName"])
    page.locator("#userEmail").fill(data["userEmail"])
    page.locator("#currentAddress").fill(data["currentAddress"])
    page.locator("#permanentAddress").fill(data["permanentAddress"])

    page.get_by_text("Submit").click()

    expect(page.locator("#name.mb-1")).to_contain_text(f"Name:{data['userName']}")
    expect(page.locator("#email.mb-1")).to_contain_text(f"Email:{data['userEmail']}")
    expect(page.locator("#currentAddress.mb-1")).to_contain_text(
        f"Current Address :{data['currentAddress']}"
    )
    expect(page.locator("#permanentAddress.mb-1")).to_contain_text(
        f"Permananet Address :{data['permanentAddress']}"
    )


@pytest.mark.pw
def test_textbox_email_error(page: Page):
    page.goto("https://demoqa.com/")
    # Query all elements with class "card mt-4 top-card" and click the first element
    page.query_selector_all(".card.mt-4.top-card")[0].click()
    page.get_by_text("Text Box").click()
    page.locator("#userEmail").fill("123")
    page.get_by_text("Submit").click()
    expect(page.locator("#userEmail")).to_have_css("border", "1px solid rgb(255, 0, 0)")


@pytest.mark.pw
def test_checkbox(page: Page):
    # Navigate to the page
    page.goto("https://demoqa.com/")
    # Query all elements with class "card mt-4 top-card" and click the first element
    page.query_selector_all(".card.mt-4.top-card")[0].click()
    # Locate the page header
    page.get_by_text("Check Box").click()
    # Locate the page header
    item_page_header = page.locator(".main-header")
    # Expect the title of the page to be "Check Box"
    expect(item_page_header).to_contain_text("Check Box")

    # Check the checkbox
    page.locator(".rct-checkbox").check()

    # Assert the checked state
    assert page.locator(".rct-checkbox").is_checked() is True
