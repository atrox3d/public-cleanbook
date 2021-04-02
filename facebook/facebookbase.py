import selenium.common.exceptions
from util.logging.loghelper import LogHelper
from util.selenium.helper import SeleniumHelper
from util.selenium.driver import DriverHelper
from util.selenium.mockdriver import MockWebDriver
from util.selenium.options import DefaultChromeOptions
try:
    from .credentials import FacebookCredentials
except ImportError:
    # run module as main
    from credentials import FacebookCredentials


import logging
logger = logging.getLogger(__name__)


class FacebookBase:
    def __init__(
            self,
            credentials: FacebookCredentials,
            seleniumhelper: SeleniumHelper,
            # facebook_home="https://www.facebook.com"
            facebook_home="https://m.facebook.com"
            # facebook_home="https://mbasic.facebook.com"
    ):
        self.credentials = credentials
        self.selenium = seleniumhelper
        self.driver = seleniumhelper.get_driver()
        self.facebook_home = facebook_home.rstrip("/")

    def home(self):
        logger.debug(f"opening home: {self.facebook_home}")
        self.selenium.new_url(self.facebook_home)

    def profile(self):
        url = f"{self.facebook_home}/{self.credentials.username}/"
        logger.debug(f"opening profile: {url}")
        self.selenium.new_url(url)

    def photos(self):
        url = f"{self.facebook_home}/{self.credentials.username}/photos_all"
        logger.debug(f"opening photos: {url}")
        self.selenium.new_url(url)

    def dismiss_cookies(self):
        #
        #   cookies
        #
        logger.info('find button by text "Accept All"...')
        btns = self.driver.find_elements_by_xpath("//*[contains(text(), 'Accept All')]")
        for btn in btns:
            try:
                logger.info('try to click "Accept All"')
                btn.click()
                logger.info('SUCCESS | click "Accept All"')
            except selenium.common.exceptions.ElementNotInteractableException as enie:
                logger.critical(f"{enie.__class__.__name__}: {enie}")
            except Exception as e:
                logger.critical(e)
                raise e

    def login(self):
        # try:
        #     logger.info('find login email field"...')
        #     email = self.driver.find_element_by_css_selector("input[type=text][name=email]")
        #     logger.info("try to edit email field...")
        #     email.send_keys(self.credentials.email)
        #     logger.info('SUCCESS | edit email field"')
        #
        #     logger.info('find login password field"...')
        #     password = self.driver.find_element_by_css_selector("input[type=password][name=pass]")
        #     logger.info("try to edit password field...")
        #     password.send_keys(self.credentials.password)
        #     logger.info('SUCCESS | edit password field"')
        #
        #     logger.info('find login login button"...')
        #     btnlogin = self.driver.find_element_by_css_selector("button[type=submit][name=login]")
        #     logger.info("try to click login button")
        #     btnlogin.click()
        #     logger.info('SUCCESS | click login"')
        #
        #     # self.selenium.wait()
        # except Exception as e:
        #     logger.critical(e)
        #     raise e
        logger.info(f"base method")

    def photos_getmenus(self):
        logger.info("search edit menus")
        edit_menus = self.driver.find_elements_by_css_selector("div[aria-haspopup=menu][aria-label=Modifica] i")
        # logger.info("print edit menus")
        # print(edit_menus)
        return edit_menus

    def photos_clickfirstmenu(self, edit_menus):
        logger.info("select first menu")
        edit_menu = edit_menus[0]
        logger.info("print edit menu")
        print(edit_menu.text)
        logger.info("click first menu")
        edit_menu.click()
        self.selenium.wait()

    def photos_getmenuitems(self):
        logger.info("search  menu items")
        menu_items = self.driver.find_elements_by_css_selector("div[role=menuitem] span")
        return menu_items

    def get_deletemenu(self, menu_items):
        menu_delete = None
        for menu_item in menu_items:
            logger.info("print menu items")
            print(menu_item.text)
            if menu_item.text == "Elimina la foto":
                menu_delete = menu_item
        return menu_delete

    def photos_clickdelete(self, menu_delete):
        logger.info("click delete photo")
        menu_delete.click()
        self.selenium.wait()

    def photos_confirmdelete(self):
        delete_photo = self.driver.find_element_by_css_selector("div[aria-label=Elimina] div span")
        delete_photo.click()
        self.selenium.wait(10)

if __name__ == '__main__':
    LogHelper.get_root_logger().setLevel(logging.INFO)
    credentials = FacebookCredentials.from_jsonfile("../myob/facebook.json")
    print(credentials)
    co = DefaultChromeOptions().get_options()
    de = DriverHelper(chrome_options=co)
    # de = MockWebDriver()
    se = SeleniumHelper(de)
    fb = FacebookBase(credentials, se)
    fb.home()
    fb.dismiss_cookies()
    fb.login()  # no
    input("press enter...")
    fb.profile()
    fb.photos()
    exit()
