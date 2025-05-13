import pytest

from contextlib import contextmanager
from _pytest.fixtures import FixtureRequest

from ui.pages.feed_page import FeedPage


class BaseCase:
    driver = None
    config = None

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.feed_page: FeedPage = (request.getfixturevalue('feed_page'))
