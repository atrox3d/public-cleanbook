from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
logger = logging.getLogger(__name__)


def wikipedia(driver: webdriver):
    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    article_count = driver.find_element_by_css_selector("#articlecount a")
    print(article_count.text)
    # article_count.click()

    all_portals = driver.find_element_by_link_text("All portals")
    # all_portals.click()

    search = driver.find_element_by_name("search")
    search.send_keys("python")
    search.send_keys(Keys.ENTER)


def login(driver: webdriver):
    driver.get("http://secure-retreat-92358.herokuapp.com/")
    driver.find_element_by_name("fName").send_keys("robb")
    driver.find_element_by_name("lName").send_keys("robbs")
    driver.find_element_by_name("email").send_keys("robb@mail.mail")
    # driver.find_element_by_css_selector(".btn-primary").click()
    driver.find_element_by_css_selector("button[type=submit]").click()


def old():
    try:
        wikipedia()
        login()
    except Exception as e:
        print(e)
