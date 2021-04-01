from util.selenium.driver import DriverHelper
from util.selenium.mockdriver import MockWebDriver
from util.selenium.options import DefaultChromeOptions
import time
import logging
logger = logging.getLogger(__name__)


class SeleniumHelper:
    def __init__(self, driver_helper: DriverHelper):
        self.driver = driver_helper.get_driver()

    def get_driver(self):
        return self.driver

    def wait(self, timeout=None):
        return
        if timeout is None:
            timeout = self.implicit_wait
        logger.info(f"waiting {timeout} seconds...")
        time.sleep(timeout)

    def new_url(self, url):
        # logger.info("sending CTRL+T")
        # driver.find_element_by_css_selector("body").send_keys(Keys.CONTROL + 't')
        logger.info(f"opening {url}")
        self.driver.get(url)
        self.wait()

    def set_timeout(self, timeout):
        self.implicit_wait = timeout

    def get_timeout(self):
        return self.implicit_wait


if __name__ == '__main__':
    driver_helper = DriverHelper()
    se = SeleniumHelper(driver_helper)
