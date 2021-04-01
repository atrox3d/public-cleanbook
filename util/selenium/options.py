from selenium import webdriver
import logging

logger = logging.getLogger(__name__)


class DefaultChromeOptions:
    def __init__(self, disable_notifications=True, start_maximized=True, *other_options):
        self.options = ()
        if disable_notifications:
            self.options += ('--disable-notifications',)
        if start_maximized:
            self.options += ('--start-maximized',)

    def get_options(self):
        logger.debug(f"initializing ChromeOptions")
        chrome_options = webdriver.ChromeOptions()

        for option in self.options:
            logger.debug(f"ChromeOptions | add {option}")
            chrome_options.add_argument(option)

        for argument in chrome_options.arguments[:]:
            logger.debug(f"ChromeOptions list | {argument}")

        return chrome_options


if __name__ == '__main__':
    options = DefaultChromeOptions()
    print(options.get_options().arguments)
