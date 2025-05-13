from ui.pages.base_page import BasePage
from ui.locators.feed_page_locators import FeedPageLocators
from ui.pages.audiences_page import AudiencesPage

from ui.pages.base_url import VKADS_BASE_URL

class FeedPage(BasePage):
    locators = FeedPageLocators()
    url = f'{VKADS_BASE_URL}/hq/overview'

    def go_to_audiences_page(self):
        self.click(self.locators.AUDIENCES_PAGE_LINK)
        return AudiencesPage(self.driver)
