#  -*- coding: utf-8 -*-
#
#  Copyright (c) 2022.
#  Created by Zhbert.
#  Licensed by GPLv3.
import time
import warnings

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from settings_file_service import *
from email_service import *

warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == '__main__':
    check_settings_file()
    chrome_options = Options()
    chrome_options.add_argument("--disable-javascript")
    # chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options, executable_path="/home/zhbert/chromedriver")
    browser.get("https://rauhfus.ru/patsientam/zapis-na-priem")
    surname = get_surname()
    name = get_name()
    middle_name = get_middle_name()
    birthday = get_birthday()
    actionChains = ActionChains(browser)
    browser.find_element_by_id('patient-surname').send_keys(surname)
    browser.find_element_by_id('patient-name').send_keys(name)
    browser.find_element_by_id('patient-second-name').send_keys(middle_name)
    filed = browser.find_element_by_id('nav-record-tab')
    browser.find_element_by_id('patient-birthday').send_keys(birthday)
    time.sleep(5)
    actionChains.move_to_element(filed).click().perform()
    browser.find_element_by_id('js-find-patient').click()
    time.sleep(5)
    actionChains.move_to_element(browser.find_element_by_id('nav-record-tab')).click().perform()
    time.sleep(5)
    actionChains.move_to_element(browser.find_element_by_css_selector('div[data-i="5"]')).click().perform()
    time.sleep(5)
    try:
        print(browser.find_element_by_class_name('alert').text)
        send_email('smtp.gmail.com', 587, 'Testing', 'from', 'to', 'Test!')
    except FileNotFoundError:
        print("Есть номерки!")
    # browser.quit()
