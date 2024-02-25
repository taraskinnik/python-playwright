from playwright.sync_api._generated import Locator

from pages.private import PrivatePage


class Channels(PrivatePage):
    @property
    def username_value_field(self) -> Locator:
        # self.menu_container.locator(".drawer-header-title")
        return self.menu_container.get_by_role("drawer-header-title")

    def navigate(self) -> None:
        self.page.goto(f"{self.base_url}/settings/channels")
