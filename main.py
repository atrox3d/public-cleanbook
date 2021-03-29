from selenium import webdriver
import time
import atexit
import logging

import util.selenium
import util.logger
from util.facebook import Facebook


#
#   root logger
#
# rootlogger = util.logger.get_cli_logger(level="INFO")
# using basic config
util.logger.setup_root_logger()
#
#   module logger
#
logger = logging.getLogger(__name__)
#
#   disable thirdparty loggers
#
util.logger.disable_loggers("urllib3", "selenium")
#
#   setup driver
#
CHROME_DRIVER_PATH = "./chromedriver"  # .exe
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)

if __name__ == "__main__":
    ############################################################################
    # enable signals in pycharm:
    # - CTRL + SHIFt + A
    # - registry
    # - kill.windows.processes.softly: true
    ############################################################################
    logger.info(f"MAIN        | atexit.register()")
    atexit.register(util.selenium.quit_handler, driver, "atexit")
    # signal.signal(signal.SIGTERM, quit_handler)
    # signal.signal(signal.SIGINT, quit_handler)

    try:
        facebook = Facebook(driver)
        facebook.home()
        facebook.dismiss_cookies()
        facebook.login()
        facebook.photos()
        util.selenium.quit_handler()
        while True:
            time.sleep(2)
    except KeyboardInterrupt as e:
        logger.critical(f"MAIN        | KeyboardInterrupt: {e}")
        # util.selenium.quit_handler(driver, KeyboardInterrupt)
        # uses atexit
    except Exception as e:
        logger.critical(f"MAIN        | {e}")

