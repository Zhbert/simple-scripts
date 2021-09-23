#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

import os
import re
import urllib.request
import zipfile

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

main_path = ""
cbz_path = ""


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
    global main_path
    global cbz_path
    browser.get(url)
    folder_name = clean_name(browser.find_element_by_class_name('name').text)
    main_path = os.path.abspath(os.curdir) + os.sep + 'LIBRARY' + os.sep + 'PIC' + os.sep + folder_name
    cbz_path = os.path.abspath(os.curdir) + os.sep + 'LIBRARY' + os.sep + 'CBZ' + os.sep + folder_name
    print('Download manga: ' + folder_name)
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
            links.append('https://mintmanga.live' + href.get('href') + '?mtr=1')
        if rate == 0:
            links.append('https://mintmanga.live' + href.get('href'))
    for link in links:
        scan_chapter(link)
    browser.quit()


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
    if not os.path.exists('LIBRARY'):
        os.mkdir('LIBRARY')
    os.chdir('LIBRARY')
    if not os.path.exists('PIC'):
        os.mkdir('PIC')
    if not os.path.exists('CBZ'):
        os.mkdir('CBZ')
    os.chdir('..')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options, executable_path="/home/zhbert/chromedriver")
    mainLink = input("Enter the main link of manga page: ")
    rate = int(input("Enter the rate of manga (0 or 1 (where 1 is a 18+)): "))
    get_chapter_links(mainLink)
    cbz_pack()
    browser.quit()
