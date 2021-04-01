import time
import logging
logger = logging.getLogger(__name__)


class SeleniumHelper:
    def __init__(
            self,
            disable_notifications=True,
            start_maximized=True,
            *options,
    ):
        logger.debug(f"setting implicit_wait to: {implicit_wait}")
        self.options = self.configure_options(disable_notifications, start_maximized, *options)
        self.driver = self.init_driver(CHROME_DRIVER_PATH, implicit_wait, self.options, self.mock_driver)

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
    se = SeleniumHelper(mock_driver=True)
