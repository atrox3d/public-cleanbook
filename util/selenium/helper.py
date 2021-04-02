from util.selenium.driver import DriverHelper
from util.selenium.mockdriver import MockWebDriver
from util.selenium.options import DefaultChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
import random
logger = logging.getLogger(__name__)

MAX_TIMEOUT = 10

class SeleniumHelper:
    def __init__(self, driver_helper: DriverHelper):
        self.driverhelper = driver_helper
        self.implicit_wait = driver_helper.implicit_wait
        self.driver = driver_helper.get_driver()

    def get_driver(self):
        return self.driver

    def wait(self, max_timeout=MAX_TIMEOUT):
        # if max_timeout is None:
        #     max_timeout = self.implicit_wait

        random_timeout = random.randint(1, max_timeout)
        for _ in range(random_timeout, 0, -1):
            logger.info(f"sleeping {_} seconds...")
            time.sleep(1)

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
