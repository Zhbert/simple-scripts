#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

import os
import re
import sys
import urllib.request
import zipfile
import warnings
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

warnings.filterwarnings("ignore", category=DeprecationWarning)

main_path = ""
main_url = ""
original_path = ""
cbz_path = ""
mainLink = ""
rate = 0
username = ""
password = ""


def scan_chapter(link):
    print(link)
    browser.get(link)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    option = soup.find('span', class_='text-cut')
    print(option)
    rx = re.compile('\.[a-zA-Z]+\?')
    if os.path.exists(option.text):
        print("The chapter exists: " + option.text)
        print("Checking the content...")
        os.chdir(option.text)
        count = browser.find_element(By.CLASS_NAME, "pages-count").text
        for counter in range(int(count)):
            print('Downloading ' + str(counter + 1) + ' from ' + count + ' in ' + option.text)
            img_url = browser.find_element(By.ID, "mangaPicture").get_attribute('src')
            match_ext = rx.search(img_url)
            ext = match_ext.group()[:-1]
            if os.path.exists(str(counter + 1) + ext):
                print("File exists. Next...")
            else:
                urllib.request.urlretrieve(img_url, str(counter) + ext)
            browser.find_element(By.CLASS_NAME, "fa-arrow-right").click()
        os.chdir('..')
    else:
        print('Creating folder: ' + option.text)
        os.mkdir(option.text)
        os.chdir(option.text)
        print('Folder created')
        count = browser.find_element(By.CLASS_NAME, "pages-count").text
        for counter in range(int(count)):
            print('Downloading ' + str(counter + 1) + ' from ' + count + ' in ' + option.text)
            img_url = browser.find_element("id", "mangaPicture").get_attribute('src')
            match_ext = rx.search(img_url)
            ext = match_ext.group()[:-1]
            urllib.request.urlretrieve(img_url, str(counter) + ext)
            browser.find_element(By.CLASS_NAME, "fa-arrow-right").click()
        os.chdir('..')


def clean_name(text):
    bad_chars = [';', ':', '!', "*", "#", '%', '&', '{', '}', '\\', '<', '>', '?', '/', '$', '\'', '"', '@', '+', '|',
                 '=']
    for i in bad_chars:
        text = text.replace(i, '')
    return text


def get_chapter_links(url):
    global main_path
    global cbz_path
    global main_url
    global username
    global password

    if "https://mintmanga.live" in url:
        main_url = "https://mintmanga.live";
    if "https://readmanga.io" in url:
        main_url = "https://readmanga.io"
    print(url)

    browser.get("https://grouple.co/internal/auth/login")
    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "password").submit()

    browser.get(url)
    folder_name = clean_name(browser.find_element(By.CLASS_NAME, "name").text)
    main_path = os.path.abspath(os.curdir) + os.sep + 'LIBRARY' + os.sep + 'PIC' + os.sep + folder_name
    cbz_path = os.path.abspath(os.curdir) + os.sep + 'LIBRARY' + os.sep + 'CBZ' + os.sep + folder_name
    print('---------------')
    print('Download manga: ' + folder_name)
    print('---------------')
    if os.path.exists(main_path):
        os.chdir(main_path)
    else:
        os.mkdir(main_path)
        os.chdir(main_path)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    hrefs = soup.find('table', class_='table table-hover').find_all('a')
    links = []
    for href in hrefs:
        if rate == 1:
            links.append(main_url + href.get('href') + '?mtr=1')
        if rate == 0:
            links.append(main_url + href.get('href'))
    for link in links:
        scan_chapter(link)
    os.chdir('..')


def cbz_pack():
    global main_path
    global cbz_path
    os.chdir(main_path)
    if not os.path.exists(cbz_path):
        os.mkdir(cbz_path)
    paths_tree = os.listdir(main_path)
    for path in paths_tree:
        os.chdir(main_path + os.sep + path)
        zip_archive = zipfile.ZipFile(cbz_path + os.sep + path + '.zip', mode='w')
        files_tree = os.listdir(os.curdir)
        for file in files_tree:
            zip_archive.write(file)
        zip_archive.close()
        os.rename(cbz_path + os.sep + path + '.zip', cbz_path + os.sep + path + '.cbz')
        os.chdir('..')


if __name__ == '__main__':
    rate = 0
    original_path = os.path.abspath(os.curdir)
    if not os.path.exists('LIBRARY'):
        os.mkdir('LIBRARY')
    os.chdir('LIBRARY')
    if not os.path.exists('PIC'):
        os.mkdir('PIC')
    if not os.path.exists('CBZ'):
        os.mkdir('CBZ')
    os.chdir('..')
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    # chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options, executable_path="/home/zhbert/chromedriver")
    if len(sys.argv) > 1:
        if "https://mintmanga.live" in sys.argv[1] or "https://readmanga.io" in sys.argv[1] != -1:
            mainLink = sys.argv[1]
        else:
            with open(sys.argv[1]) as file:
                lines = file.readlines()
                count = 0
                for line in lines:
                    os.chdir(original_path)
                    if re.match('^[\w:\/\.\-]+ \d', line):
                        params = line.split()
                        mainLink = params[0]
                        rate = int(params[1])
                        get_chapter_links(mainLink)
                        cbz_pack()
                print("All done. Enjoy!")
            sys.exit()
        if len(sys.argv) > 2:
            if sys.argv[2].isnumeric():
                if int(sys.argv[2]) == 1:
                    rate = int(sys.argv[2])
                else:
                    print('Invalid rating value!')
                    sys.exit()
            else:
                print('Invalid rating value')
                sys.exit()
        else:
            print("Error: rating is not specified!")
            sys.exit()
    else:
        mainLink = input("Enter the main link of manga page: ")
        rate = int(input("Enter the rate of manga (0 or 1 (where 1 is a 18+)): "))
        get_chapter_links(mainLink)
        cbz_pack()
        print("All done. Enjoy!")
    browser.quit()
