from playwright.sync_api._generated import Locator

from pages.base import Base


class Login(Base):
    @property
    def userform(self) -> Locator:
        # return self.page.locator(".login")
        return self.page.get_by_role("login")
    
    @property
    def password_field(self) -> Locator:
        # return self.userform.locator(".password")
        return self.page.get_by_role("password")

    @property
    def submit_button(self) -> Locator:
        # return self.userform.locator(".submit")
        return self.page.get_by_role("submit")

    @property
    def username_field(self) -> Locator:
        # return self.userform.locator(".text")
        return self.page.get_by_role("text")

    def fill_form(self, user: dict) -> None:
        """Fill out the login form.

        :param user: A user intended for login.
        """
        self.username_field.fill(user["userName"])
        self.password_field.fill(user["password"])

    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}/login")
