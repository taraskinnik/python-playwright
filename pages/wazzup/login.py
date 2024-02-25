from playwright.sync_api._generated import Locator

from pages.base import Base


class Login(Base):
    @property
    def userform(self) -> Locator:
        return self.page.locator(".login")
    
    @property
    def password_field(self) -> Locator:
        return self.userform.get_by_label("Password")

    @property
    def submit_button(self) -> Locator:
        return self.userform.get_by_role("button", name="Log in")

    @property
    def username_field(self) -> Locator:
        return self.userform.get_by_label("Email")

    def fill_form(self, user: dict) -> None:
        """Fill out the login form.

        :param user: A user intended for login.
        """
        self.username_field.fill(user["userName"])
        self.password_field.fill(user["password"])

    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}/login")
