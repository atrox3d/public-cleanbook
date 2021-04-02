import atexit
from selenium import webdriver
from util.selenium.mockdriver import MockWebDriver
from util.selenium.options import DefaultChromeOptions
from util.system.systemhelper import SystemHelper
import logging

logger = logging.getLogger(__name__)

try:
    if __name__ == '__main__':
        CHROME_DRIVER_PATH = "../../chromedriver"  # .exe
    else:
        CHROME_DRIVER_PATH = "../chromedriver"  # .exe
except:
    CHROME_DRIVER_PATH = "./chromedriver"  # .exe

IMPLICIT_WAIT = 10


class DriverHelper:
    def __init__(
            self,
            driver_path=CHROME_DRIVER_PATH,
            implicit_wait=IMPLICIT_WAIT,
            chrome_options=DefaultChromeOptions().get_options(),
            kill_onexit=True,
            mock_driver=False
    ):
        self.driver_path = driver_path
        self.implicit_wait = implicit_wait
        self.chrome_options = chrome_options
        self.mock_driver = mock_driver
        self.kill_onexit = kill_onexit

        self.driver = None
        self.init_driver()

        logger.debug(f"kill_driver is {'enabled' if kill_onexit else 'disabled'}")
        if kill_onexit:
            self.on_quit(self.kill_chromedriver, "on_quit")


    def init_driver(self):
        if self.mock_driver:
            logger.debug(f"initializing MockWebDriver")
            self.driver = MockWebDriver()
        else:
            logger.debug(f"initializing ChromeDriver")
            self.driver = webdriver.Chrome(self.driver_path, options=self.chrome_options)

        logger.debug(f"setting implicit_wait to: {self.implicit_wait}")
        self.driver.implicitly_wait(self.implicit_wait)

    def kill_chromedriver(self, cause):
        logger.info(f"QUIT_HANDLER| intercepted {cause}")
        logger.info(f"QUIT_HANDLER| quitting chromedriver...")
        self.driver.quit()

        logger.info(f"QUIT_HANDLER| done.")
        logger.info(f"QUIT_HANDLER| taskkill")
        SystemHelper.taskkill()

        logger.info(f"QUIT_HANDLER| tasklist")
        SystemHelper.tasklist()

    @staticmethod
    def on_quit(handler, *args):
        ############################################################################
        # enable signals in pycharm:
        # - CTRL + SHIFt + A
        # - registry
        # - kill.windows.processes.softly: true
        ############################################################################
        str_args = tuple(arg if type(arg) == str else arg.__class__ for arg in args)
        logger.info(f"MAIN        | atexit.register({handler.__name__}, {str_args})")
        atexit.register(handler, *args)
        # signal.signal(signal.SIGTERM, quit_handler)
        # signal.signal(signal.SIGINT, quit_handler)

    def get_driver(self):
        return self.driver