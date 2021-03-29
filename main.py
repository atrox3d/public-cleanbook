from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import atexit
import util.system
import util.selenium
import util.logger
import logging

# rootlogger = util.logger.get_cli_logger(level="INFO")
util.logger.setup_root_logger()
logger = logging.getLogger(__name__)
util.logger.disable_loggers("urllib3", "selenium")


CHROME_DRIVER_PATH = "./chromedriver"  # .exe
driver = webdriver.Chrome(CHROME_DRIVER_PATH)


if __name__ == "__main__":
    """
        enable signals in pycharm:
        - CTRL + SHIFt + A
        - registry
        - kill.windows.processes.softly: true
    """
    logger.info(f"MAIN        | atexit.register()")
    atexit.register(util.selenium.quit_handler, driver, "atexit")
    # signal.signal(signal.SIGTERM, quit_handler)
    # signal.signal(signal.SIGINT, quit_handler)

    try:
        driver.get("https://www.facebook.com/")
        time.sleep(2)
    except KeyboardInterrupt as e:
        logger.critical(f"MAIN        | KeyboardInterrupt: {e}")
        # util.selenium.quit_handler(driver, KeyboardInterrupt)
        # uses atexit
    except Exception as e:
        logger.exception(f"MAIN        | {e}")

