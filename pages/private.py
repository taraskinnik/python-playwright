from playwright.sync_api._generated import Locator

from pages.base import Base


class PrivatePage(Base):
    @property
    def menu_container(self) -> Locator:
        # return self.page.locator(".drawer-menu-container")
        return self.page.get_by_role("drawer-menu-container")
