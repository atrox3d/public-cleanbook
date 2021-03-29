from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import logging
import myob.facebook

logger = logging.getLogger(__name__)


def dismiss_cookies(driver: webdriver.Chrome):
    #
    #   cookies
    #
    logger.info('find button "Accept All"...')
    btns_acceptall = driver.find_elements_by_xpath("//*[contains(text(), 'Accept All')]")
    for btn in btns_acceptall:
        try:
            logger.info('try to click "Accept All"')
            btn.click()
            logger.info('SUCCESS | click "Accept All"')
        except selenium.common.exceptions.ElementNotInteractableException as enie:
            logger.critical(f"{enie.__class__.__name__}: {enie}")
        except Exception as e:
            logger.critical(e)
            raise e


def login_home(driver: webdriver.Chrome):
    #
    #   login
    #
    # driver.find_element_by_css_selector("button[type=submit]").click()
    try:
        logger.info('find login email field"...')
        email = driver.find_element_by_css_selector("input[type=text][name=email][id=email]")
        logger.info("try to edit email field...")
        email.send_keys(myob.facebook.EMAIL)
        logger.info('SUCCESS | edit email field"')

        logger.info('find login password field"...')
        password = driver.find_element_by_css_selector("input[type=password][name=pass][id=pass]")
        logger.info("try to edit password field...")
        password.send_keys(myob.facebook.PASSWORD)
        logger.info('SUCCESS | edit password field"')

        logger.info('find login login button"...')
        btnlogin = driver.find_element_by_css_selector("button[type=submit][name=login]")
        logger.info("try to click login button")
        btnlogin.click()
        logger.info('SUCCESS | click login"')

    except Exception as e:
        logger.critical(e)


def login_profile(driver: webdriver.Chrome):
    #
    #   login
    #
    # driver.find_element_by_css_selector("button[type=submit]").click()
    try:
        logger.info('find login email field"...')
        email = driver.find_element_by_css_selector("input[type=email][name=email]")
        logger.info("try to edit email field...")
        email.send_keys(myob.facebook.EMAIL)
        logger.info('SUCCESS | edit email field"')

        logger.info('find login password field"...')
        password = driver.find_element_by_css_selector("input[type=password][name=pass]")
        logger.info("try to edit password field...")
        password.send_keys(myob.facebook.PASSWORD)
        logger.info('SUCCESS | edit password field"')

        logger.info('find login login button"...')
        btnlogin = driver.find_element_by_css_selector("button[type=submit][name=login]")
        logger.info("try to click login button")
        btnlogin.click()
        logger.info('SUCCESS | click login"')

    except Exception as e:
        logger.critical(e)
