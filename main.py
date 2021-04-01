import time
import logging
import sys

from util.seleniumhelper import SeleniumHelper
from util.loghelper import LogHelper
# from facebook.facebook import Facebook
from facebook import FacebookFactory
import myob.facebook

if __name__ == "__main__":
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
    seleniumhelper = SeleniumHelper(mock_driver=True)
    try:
        facebook = FacebookFactory.get_facebook(
            seleniumhelper,
            myob.facebook.EMAIL,
            myob.facebook.PASSWORD,
            myob.facebook.USER,
            # "https://www.facebook.com"
            "https://mbasic.facebook.com"
        )
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
