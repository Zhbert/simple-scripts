#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

import os
import re
import urllib.request
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


def scan_chapter(link):
    browser.get(link)
    select = Select(browser.find_element_by_id('chapterSelectorSelect'))
    option = select.first_selected_option
    rx = re.compile('\.[a-zA-Z]+\?')
    if os.path.exists(option.text):
        print("The chapter exists: " + option.text)
        print("Checking the content...")
        os.chdir(option.text)
        count = browser.find_element_by_class_name('pages-count').text
        for counter in range(int(count)):
            print('Downloading ' + str(counter + 1) + ' from ' + count + ' in ' + option.text)
            img_url = browser.find_element_by_id('mangaPicture').get_attribute('src')
            match_ext = rx.search(img_url)
            ext = match_ext.group()[:-1]
            if os.path.exists(str(counter + 1) + ext):
                print("File exists. Next...")
            else:
                urllib.request.urlretrieve(img_url, str(counter) + ext)
            browser.find_element_by_class_name('fa-arrow-right').click()
        os.chdir('..')
    else:
        print('Creating folder: ' + option.text)
        os.mkdir(option.text)
        os.chdir(option.text)
        print('Folder created')
        count = browser.find_element_by_class_name('pages-count').text
        for counter in range(int(count)):
            print('Downloading ' + str(counter + 1) + ' from ' + count + ' in ' + option.text)
            img_url = browser.find_element_by_id('mangaPicture').get_attribute('src')
            match_ext = rx.search(img_url)
            ext = match_ext.group()[:-1]
            urllib.request.urlretrieve(img_url, str(counter) + ext)
            browser.find_element_by_class_name('fa-arrow-right').click()
        os.chdir('..')


def clean_name(text):
    bad_chars = [';', ':', '!', "*", "#", '%', '&', '{', '}', '\\', '<', '>', '?', '/', '$', '\'', '"', '@', '+', '|',
                 '=']
    for i in bad_chars:
        text = text.replace(i, '')
    return text


def get_chapter_links(url):
    browser.get(url)
    folder_name = clean_name(browser.find_element_by_class_name('name').text)
    print('Download manga: ' + folder_name)
    if os.path.exists(folder_name):
        os.chdir(folder_name)
    else:
        os.mkdir(folder_name)
        os.chdir(folder_name)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    hrefs = soup.find('table', class_='table table-hover').find_all('a')
    links = []
    for href in hrefs:
        if rate == 1:
            links.append('https://mintmanga.live' + href.get('href') + '?mtr=1')
        if rate == 0:
            links.append('https://mintmanga.live' + href.get('href'))
    for link in links:
        scan_chapter(link)
    browser.quit()


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options, executable_path="/home/zhbert/chromedriver")
    mainLink = input("Enter the main link of manga page: ")
    rate = int(input("Enter the rate of manga (0 or 1 (where 1 is a 18+)): "))
    get_chapter_links(mainLink)
    browser.quit()
