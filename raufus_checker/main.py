#  -*- coding: utf-8 -*-
#
#  Copyright (c) 2022.
#  Created by Zhbert.
#  Licensed by GPLv3.
import warnings

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from settings_file_service import *

warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == '__main__':
    check_settings_file()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options, executable_path="/home/zhbert/chromedriver")
    browser.get("https://rauhfus.ru/patsientam/zapis-na-priem")
    surname = get_surname()
    name = get_name()
    middle_name = get_name()
    birthday = get_birthday()
    browser.quit()

