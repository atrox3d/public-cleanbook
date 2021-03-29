from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import atexit
import util.system
import util.selenium
import util.logger

rootlogger = util.logger.get_cli_logger()


CHROME_DRIVER_PATH = "./chromedriver"  # .exe
driver = webdriver.Chrome(CHROME_DRIVER_PATH)


if __name__ == "__main__":
    """
        enable signals in pycharm:
        - CTRL + SHIFt + A
        - registry
        - kill.windows.processes.softly: true
    """
    print(f"MAIN        | atexit.register()")
    atexit.register(util.selenium.quit_handler, driver, "atexit")
    # signal.signal(signal.SIGTERM, quit_handler)
    # signal.signal(signal.SIGINT, quit_handler)

    try:
        driver.get("https://www.facebook.com/")
        time.sleep(2)
    except KeyboardInterrupt as e:
        print(f"MAIN        | KeyboardInterrupt: {e}")
        # util.selenium.quit_handler(driver, KeyboardInterrupt)
        # uses atexit
    except Exception as e:
        print(f"MAIN        | {e}")

