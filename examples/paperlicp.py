import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint

CHROME_DRIVER_PATH = "c:/Users/***REMOVED***/code/python/100-days-of-code/chromedriver"  # .exe
driver = webdriver.Chrome(CHROME_DRIVER_PATH)


def get_button(selector):
    tag = driver.find_element_by_css_selector(selector)
    return tag


def get_text(selector):
    tag = driver.find_element_by_css_selector(selector)
    text = tag.text
    return text


def get_int(money_text: str):
    money_text = money_text.replace(",", "")
    return int(money_text)


def get_float(money_text: str):
    money_text = money_text.replace(",", "")
    return float(money_text)


def get_paperclips():
    text = get_text("#clips")
    value = get_int(text)
    return value


def get_funds():
    text = get_text("#funds")
    value = get_float(text)
    return value


def get_unsold():
    text = get_text("#unsoldClips")
    value = get_int(text)
    return value


def get_priceperclip():
    text = get_text("#margin")
    value = get_float(text)
    return value


def get_demand():
    text = get_text("#demand")
    value = get_int(text)
    return value


def get_wire():
    text = get_text("#wire")
    value = get_int(text)
    return value


def get_wire_price():
    text = get_text("#wireCost")
    value = get_int(text)
    return value


driver.get("https://www.decisionproblem.com/paperclips/index2.html")
paperclip = driver.find_element_by_css_selector("#btnMakePaperclip")

SECONDS = 5

try:
    print("while True")
    while True:
        time_start = time.time()
        print(f"while click for {SECONDS} seconds")
        while time.time() < time_start + 5:
            paperclip.click()

        paperclips = get_paperclips()
        funds = get_funds()
        unsold = get_unsold()
        priceperclip = get_priceperclip()
        demand = get_demand()
        wire = get_wire()
        wire_price = get_wire_price()
        print(f"current paperclips: {paperclips}")
        print(f"current funds     : {funds}")
        print(f"unsold clips      : {unsold}")
        print(f"price per clip    : {priceperclip}")
        print(f"public demand     : {demand}")
        print(f"wire              : {wire}")
        print(f"wire price        : {wire_price}")

        buywire = get_button("#btnBuyWire")
        print("buywire: ", buywire.is_enabled())
        if wire == 0 and buywire.is_enabled():
            buywire.click()


        time.sleep(2)
except selenium.common.exceptions.WebDriverException as wde:
    print(wde)
