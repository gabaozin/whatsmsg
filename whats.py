"""
Disclaimer: This script is just for educational purpose
"""

# Here is the list of all modules needed for the code to work.
# You can install selenium and openpyxl using pip.

import csv

# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Here's how to pull name info from a CSV file. Specify PATH to your .csv file.
try:
    with open("contacts.csv") as f:
        reader = csv.DictReader(f)
        contacts = [dict(row) for row in reader]
except FileNotFoundError:
    contacts = []


# Personalised message, change at will.
# Template = Hi + first name + rest of message (multi-line)

greeting = "Hi "
message = """, is everything allright?

I hope you are doing great!

Sending this message to light up your day.

Cheers!!"""

# Calls browser (using Chrome but you can choose browser at will. See selenium documentation),
# web whatsapp page and then waits on your input(ok) to continue the program.
# driver = webdriver.Chrome("PATH_TO_CHROMEDRIVER")
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("Click when QR code done")

# Rapid Tables Notepad is a good page to test changes in the code without bothering people.
# Uncomment lines 58, 62 and 65 and comment lines 53, 54, 61 and 64 to use this other website.
# Do the opposite to come back to whatsapp.

# driver.get('https://www.rapidtables.com/tools/notepad.html')

for contact in contacts:
    # name = contact.get("name", "").split(" ")[0]
    name = contact.get("name", "")

    search_box = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')
        )
    )
    # search_box = driver.find_element_by_id('area')
    search_box.send_keys(name + Keys.ENTER)
    input_box = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    )
    # input_box = driver.find_element_by_id("area")
    input_box.send_keys(greeting + name)
    for line in message.split("\n"):
        ActionChains(driver).send_keys(line).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(
            Keys.SHIFT
        ).key_up(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.RETURN).perform()
