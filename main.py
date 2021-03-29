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

        logger.info("search edit menus")
        edits = driver.find_elements_by_css_selector("div[aria-haspopup=menu][aria-label=Modifica] i")
        logger.info("print edit menus")
        print(edits)
        logger.info("search edit menus text")
        for edit in edits:
            print(edit.text)
        logger.info("select first menu")
        edit = edits[0]
        logger.info("print edit menu")
        print(edit.text)
        logger.info("click first menu")
        edit.click()
        util.selenium.wait()
        logger.info("search  menu items")
        menu_items = driver.find_elements_by_css_selector("div[role=menuitem] span")
        menu_delete = None
        for menu_item in menu_items:
            logger.info("print menu items")
            print(menu_item.text)
            if menu_item.text == "Elimina la foto":
                menu_delete = menu_item

        logger.info("click delete photo")
        menu_delete.click()
        util.selenium.wait()
        delete_photo = driver.find_element_by_css_selector("div[aria-label=Elimina] div span")
        delete_photo.click()

        while True:
            util.selenium.wait()
        # util.selenium.quit_handler()
    except KeyboardInterrupt as e:
        logger.critical(f"MAIN        | KeyboardInterrupt: {e}")
        # util.selenium.quit_handler(driver, KeyboardInterrupt)
        # uses atexit
    except Exception as e:
        logger.critical(f"MAIN        | {e}")
