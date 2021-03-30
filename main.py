from selenium import webdriver
import time
import atexit
import logging

from util.seleniumhelper import SeleniumHelper
from util.loghelper import LogHelper
from util.facebook import Facebook

#
#   root logger
#
# using basic config
LogHelper.get_root_logger()
#
#   module logger
#
logger = logging.getLogger(__name__)
#
#   disable thirdparty loggers
#
LogHelper.disable_loggers("urllib3", "selenium")
#
#   setup driver
#
CHROME_DRIVER_PATH = "./chromedriver"  # .exe
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)

seleniumhelper = SeleniumHelper(driver)

if __name__ == "__main__":
    ############################################################################
    # enable signals in pycharm:
    # - CTRL + SHIFt + A
    # - registry
    # - kill.windows.processes.softly: true
    ############################################################################
    logger.info(f"MAIN        | atexit.register()")
    atexit.register(seleniumhelper.quit_handler, "atexit")
    # signal.signal(signal.SIGTERM, quit_handler)
    # signal.signal(signal.SIGINT, quit_handler)

    try:
        facebook = Facebook(driver)
        facebook.home()
        facebook.dismiss_cookies()
        facebook.login()
        facebook.photos()
        more_photos = True
        while more_photos:
            try:
                edit_menus = facebook.photos_getmenus()
                if len(edit_menus):
                    more_photos = True
                else:
                    logger.info("NO MORE PHOTOS!")
                    more_photos = False
                facebook.photos_clickfirstmenu(edit_menus)
                menu_items = facebook.photos_getmenuitems()
                menu_delete = facebook.get_deletemenu(menu_items)
                facebook.photos_clickdelete(menu_delete)
                facebook.photos_confirmdelete()

            except Exception as e:
                logger.critical(e)
                continue
        while True:
            seleniumhelper.wait()
    except KeyboardInterrupt as e:
        logger.critical(f"MAIN        | KeyboardInterrupt: {e}")
        # util.selenium.quit_handler(driver, KeyboardInterrupt)
        # uses atexit
    except Exception as e:
        logger.critical(f"MAIN        | {e}")
