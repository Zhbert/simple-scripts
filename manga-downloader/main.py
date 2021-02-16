#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests as req
import os
import time

from selenium.webdriver.support.select import Select


def scan_chapter(link):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)
    select = Select(browser.find_element_by_id('chapterSelectorSelect'))
    option = select.first_selected_option
    print('Creating folder: ' + option.text)
    os.mkdir(option.text)
    browser.quit()
    print('Folder created. Timeout...')
    time.sleep(5)


def clean_name(text):
    bad_chars = [';', ':', '!', "*", "#", '%', '&', '{', '}', '\\', '<', '>', '?', '/', '$', '\'', '"', '@', '+', '|',
                 '=']
    for i in bad_chars:
        text = text.replace(i, '')
    return text


def get_chapter_links(url):
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    folderName = clean_name(soup.find('span', class_='name').text)
    if os.path.exists(folderName):
        os.chdir(folderName)
    else:
        os.mkdir(folderName)
        os.chdir(folderName)
    hrefs = soup.find('table', class_='table table-hover').find_all('a')
    if os.path.exists('chaptesLinks.txt'):
        os.remove('chaptesLinks.txt')
    file = open('chaptesLinks.txt', 'w')
    for href in hrefs:
        if rate == 1:
            file.write('https://mintmanga.live' + href.get('href') + '?mtr=1' + '\n')
        if rate == 0:
            file.write('https://mintmanga.live' + href.get('href') + '\n')
    file.close()


if __name__ == '__main__':
    mainLink = input("Enter the main link of manga page: ")
    rate = int(input("Enter the rate of manga (0 or 1 (where 1 is a 18+)): "))
    get_chapter_links(mainLink)
    if os.path.exists('chaptesLinks.txt'):
        with open('chaptesLinks.txt') as file:
            lines = file.readlines();
        for line in lines:
            scan_chapter(line)