from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

browser = webdriver.Firefox()
login_url = "https://ep.ups.com/UPSRegistration/UPSLogin"
ChecksUrl = "https://gems-ss.ups.com/psc/hrprod/EMPLOYEE/HRMS/c/M_UPS_MENU.PAYCHECK_VW_FLU.GBL"

browser.get(login_url)
time.sleep(10)
username = browser.find_element_by_id("userName")
password = browser.find_element_by_id("password")
username.send_keys("USERNAME")
password.send_keys("PASSWORD")


login_attempt = browser.find_element_by_class_name("btn")
login_attempt.send_keys(Keys.RETURN)
time.sleep(30)


def write_to_file(file, data):
    with open(file, 'w') as file_interface:
        file_interface.write(data)


browser.get(ChecksUrl)
time.sleep(5)
checks_table = browser.find_element_by_class_name("ps_grid-flex")
tbl = checks_table.get_attribute("outerHTML")
df = pd.read_html(tbl)

i = 0
while i < len(df[0]):

    paycheck_number = df[0]['Paycheck Number'][i]
    filename = r"C:\Temp\retropay\{}.html".format(paycheck_number)
    browser.execute_script("javascript:submitAction_win0(document.win0,'VIEW_PAY${}');".format(i))
    time.sleep(3)
    i += 1
    html = browser.page_source
    write_to_file(file=filename, data=html)
    browser.execute_script("history.back()")
    time.sleep(3)
