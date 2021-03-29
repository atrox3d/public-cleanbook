from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import logging

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


def login(driver: webdriver.Chrome):
    #
    #   login
    #
    # driver.find_element_by_css_selector("button[type=submit]").click()
    logger.info('find login email field"...')
    try:
        email = driver.find_element_by_css_selector("input[type=text][name=email][id=email]")
        logger.info("try to edit email field...")
        email.send_keys("ciaociao")
        logger.info('SUCCESS | edit email field"')

        password = driver.find_element_by_css_selector("input[type=password][name=pass][id=pass]")
        logger.info("try to edit password field...")
        password.send_keys("ciaociao")
        logger.info('SUCCESS | edit password field"')

    except Exception as e:
        logger.critical(e)
