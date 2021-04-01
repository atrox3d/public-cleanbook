import logging
import sys

from util.selenium.helper import SeleniumHelper
from util.selenium.driver import DriverHelper
from util.logging.loghelper import LogHelper
from facebook import FacebookFactory
from facebook.credentials import FacebookCredentials

#
#   root logger
#
# using basic config
rootlogger = LogHelper.get_root_logger()
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
driverhelper = DriverHelper(mock_driver=False)
seleniumhelper = SeleniumHelper(driverhelper)
credentials = FacebookCredentials.from_jsonfile("myob/facebook.json")
try:
    facebook = FacebookFactory.get_facebook(seleniumhelper, **credentials, facebook_home="https://mbasic.facebook.com")
    facebook.home()
    facebook.dismiss_cookies()
    facebook.login()
    input("press a key to quit")
    exit()
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
    logger.critical(f"MAIN        | Exception: {e}")
    logger.critical(f"MAIN        | Exception: {sys.exc_info()}")
