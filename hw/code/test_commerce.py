from base import BaseCase
from ui.fixtures import *

from _pytest.fixtures import FixtureRequest


class TestCommerce(BaseCase):
    def test_commerce(self, request: FixtureRequest):
        page = request.getfixturevalue('commerce_page')
        page.open()
        import time; time.sleep(10)
