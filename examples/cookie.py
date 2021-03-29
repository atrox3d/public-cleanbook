import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint

CHROME_DRIVER_PATH = "c:/Users/***REMOVED***/code/python/100-days-of-code/chromedriver"  # .exe
driver = webdriver.Chrome(CHROME_DRIVER_PATH)


def get_money_value(money_text: str):
    money_text = money_text.replace(",", "")
    return int(money_text)


def get_money():
    money_tag = driver.find_element_by_css_selector("#money")
    money_text = money_tag.text
    money_value = get_money_value(money_text)
    return money_value


def get_price(tag_id):
    tag = driver.find_element_by_css_selector(tag_id)
    text = tag.text.split(" - ")[1]
    value = get_money_value(text)
    return {value: tag}


def get_upgrades() -> dict:
    upgrades = {}
    upgrades.update(get_price("#buyCursor b"))
    upgrades.update(get_price("#buyGrandma b"))
    upgrades.update(get_price("#buyFactory b"))
    upgrades.update(get_price("#buyMine b"))
    upgrades.update(get_price("#buyShipment b"))
    upgrades.update(get_price("div[id='buyAlchemy lab'] b"))
    upgrades.update(get_price("#buyPortal b"))
    upgrades.update(get_price("div[id='buyTime machine'] b"))
    return upgrades


driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_css_selector("#cookie")

try:
    print("while True")
    while True:
        time_start = time.time()
        print("while click")
        while time.time() < time_start + 5:
            cookie.click()

        print("get prices")
        money = get_money()
        upgrades = get_upgrades()

        to_buy = None
        for price, tag in upgrades.items():
            if money >= price:
                to_buy = tag

        if to_buy:
            print(f"buy {to_buy.text}")
            to_buy.click()

        # print("exit()")
        # driver.quit()
        # exit()
        # time.sleep(2)
except selenium.common.exceptions.WebDriverException as wde:
    print(wde)
