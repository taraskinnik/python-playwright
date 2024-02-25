import pytest
from playwright.sync_api import Page

from credentials import user
from pages import Login, Channels


@pytest.mark.authentication
@pytest.mark.bookstore
class TestLogin:
    def test_valid_login(self, page: Page) -> None:
        """Login with valid credentials.

        :param page: A Playwright browser page.
        """
        page.context.clear_cookies()
        login_page = Login(page)
        channels_page = Channels(page)

        login_page.navigate()
        login_page.fill_form(user)
        login_page.submit_button.click()

        expect(channels_page.username_value_field).to_have_text("Wazzup: 9496-6880")

        with page.expect_response("**/BookStore/v1/Books") as response:
            books_page.navigate()

        visible: bool = books_page.book(title=book_title).is_visible()

        assert visible and response.value.ok
