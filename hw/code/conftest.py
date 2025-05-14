from ui.pages.base_url import VKADS_BASE_URL
from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default=VKADS_BASE_URL)
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
    }


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "needs_audience: mark test as requiring pre-created audience"
    )
