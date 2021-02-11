#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from bs4 import BeautifulSoup
from selenium import webdriver
import requests as req
import os


def scan_chapter(link):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)
    print(browser.find_element_by_id('mangaPicture').get_attribute('src'))
    generated_html = browser.page_source
    browser.quit()
    file = open('html', 'w')
    file.write(generated_html)


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
    os.mkdir(folderName)
    os.chdir(folderName)
    hrefs = soup.find('table', class_='table table-hover').find_all('a')
    file = open('chaptesLinks.txt', 'w')
    for href in hrefs:
        file.write('https://mintmanga.live' + href.get('href') + '?mtr=1' + '\n')
    file.close()


if __name__ == '__main__':
    get_chapter_links(
        'https://mintmanga.live/mag_celitel__novyi_start___vysshee_iscelenie__chary_momentalnoi_smerti_i_kraja_umenii')
    scan_chapter('https://mintmanga.live/mag_celitel__novyi_start___vysshee_iscelenie__chary_momentalnoi_smerti_i_kraja_umenii/vol8/64?mtr=1')