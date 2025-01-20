import pytest
from selene import browser

from utils.configure import Configure
from utils.util import get_driver, add_screenshot, add_html, add_video


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver = get_driver()
    browser.config.base_url = Configure.base_url
    browser.config.timeout = 10

    yield

    add_screenshot(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()
