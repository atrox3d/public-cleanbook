from selenium import webdriver
import pprint
from json import dumps

CHROME_DRIVER_PATH = "c:/Users/***REMOVED***/code/python/100-days-of-code/chromedriver"  # .exe
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


def get_amazon_price():
    driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB")
    price = driver.find_element_by_id("priceblock_ourprice")
    print(price.text)


driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
pprint.pprint(event_times)
print(type(event_times))

event_names = driver.find_elements_by_css_selector(".event-widget .menu a")
pprint.pprint(event_names)
print(type(event_names))

for time in event_times:
    print(time.text)

for name in event_names:
    print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

pprint.pprint(events, indent=4)
print(dumps(events, indent=4))
#
#
#
driver.quit()
