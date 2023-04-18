import os
import re
import sys
import urllib.request
import zipfile
import warnings
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from fake_useragent import UserAgent

option = webdriver.FirefoxOptions()
# убирает флажок что автоматизированное ПО управляет браузером
option.set_preference("dom.webdriver.enabled", False)
# подмена user-agent
ua = UserAgent()
us_ag = ua.random
option.set_preference("general.useragent.override", us_ag)
# chrome_options.add_argument('--headless')
browser = webdriver.Firefox(options=option, executable_path="/home/zhbert/geckodriver")

browser.get("https://grouple.co/internal/auth/login")
browser.find_element(By.ID, "username").send_keys("")
browser.find_element(By.ID, "password").send_keys("")
browser.find_element(By.ID, "password").submit()
time.sleep(30)

browser.get('https://mintmanga.live/diavolenok_v_moei_vlasti/vol1/7?mtr=1')
time.sleep(30)