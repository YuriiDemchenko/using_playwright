import pytest
from playwright.sync_api import Page, expect


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
    # Query all elements with class "card mt-4 top-card" and click the first element
    page.query_selector_all(".card.mt-4.top-card")[0].click()
    page.get_by_text("Text Box").click()
    page.locator("#userEmail").fill("123")
    page.get_by_text("Submit").click()
    expect(page.locator("#userEmail")).to_have_css("border", "1px solid rgb(255, 0, 0)")


@pytest.mark.pw
def test_checkbox(page: Page):
    items_to_select = ["General", "Notes", "React"]
    # Query all elements with class "card mt-4 top-card" and click the first element
    page.query_selector_all(".card.mt-4.top-card")[0].click()
    # Locate the page header
    page.get_by_text("Check Box").click()
    # Locate the page header
    item_page_header = page.locator(".main-header")
    # Expect the title of the page to be "Check Box"
    expect(item_page_header).to_contain_text("Check Box")

    page.get_by_label("Expand all").click()
    # Check the checkbox
    page.get_by_text("Home", exact=True).check()
    # Assert the checked state
    assert page.get_by_text("Home", exact=True).is_checked() is True
    for i in page.locator(".rct-checkbox").all():
        i.uncheck()
    assert page.get_by_text("Downloads", exact=True).is_checked() is False
    page.get_by_label("Expand all").click()

    for item in items_to_select:
        page.get_by_text(item, exact=True).check()
        assert page.get_by_text(item, exact=True).is_checked() is True

    page.get_by_label("Collapse all").click()


@pytest.mark.pw
def test_radio_buttons(page: Page):
    page.get_by_text("Elements").click()
    # Locate the page header
    page.get_by_text("Radio Button").click()
    # Locate the page header
    item_page_header = page.locator(".main-header")
    # Expect the title of the page to be "Radio Button"
    expect(item_page_header).to_contain_text("Radio Button")
    page.get_by_text("Yes").click()
    assert page.locator("#yesRadio").is_checked() is True
    assert page.locator(".text-success").text_content() == "Yes"
    page.get_by_text("Impressive").click()
    assert page.locator("#impressiveRadio").is_checked() is True
    assert page.locator(".text-success").text_content() == "Impressive"
    expect(page.locator("#noRadio")).to_be_disabled()


@pytest.mark.pw1
def test_web_tables(page: Page):
    page.get_by_text("Elements").click()
    page.get_by_text("Web Tables").click()
    page.locator("#addNewRecordButton").click()
    # Fill all fields
    page.get_by_placeholder("First Name").fill("John")
    page.get_by_placeholder("Last Name").fill("Doe")
    page.get_by_placeholder("name@example.com").fill("j.d@fake.com")
    page.get_by_placeholder("Age").fill("19")
    page.get_by_placeholder("Salary").fill("999")
    page.get_by_placeholder("Department").fill("IT")
    page.get_by_text("Submit").click()
    # Expect selected fields to have correct values
    expect(page.locator(".rt-table")).to_contain_text("John")
    expect(page.locator(".rt-table")).to_contain_text("Doe")
    expect(page.locator(".rt-table")).to_contain_text("j.d@fake.com")
    expect(page.locator(".rt-table")).to_contain_text("19")
    expect(page.locator(".rt-table")).to_contain_text("999")
    expect(page.locator(".rt-table")).to_contain_text("IT")

    # Edit selected record
    find_element(page, "John", "edit").click()
    page.get_by_placeholder("Salary").fill("1520")
    page.get_by_placeholder("Department").fill("Support")
    page.get_by_text("Submit").click()

    # Delete selected record
    find_element(page, "John", "delete").click()


def find_element(page: Page, name, action):
    # Get the locator for all rows in the table
    rows_locator = page.locator(".rt-table .rt-tbody .rt-tr-group")
    # Get the number of rows
    num_rows = rows_locator.count()
    # Iterate over each row
    for i in range(num_rows):
        # Get the locator for the current row
        row = rows_locator.nth(i)
        # Get the first name in the current row
        first_name = row.locator(".rt-td").nth(0).inner_text()
        # Check if the first name matches the name we're looking for
        if first_name == name:
            # If it does, return the locator for the element with the specified action in the current row
            return row.locator(f"span[id^='{action}-record-']")
            # Exit the loop once the element is found
            break
