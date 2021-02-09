#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from bs4 import BeautifulSoup
import requests as req


def get_chapter_links(url):
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    hrefs = soup.find('table', class_='table table-hover').find_all('a')
    file = open('links.txt', 'w')
    for href in hrefs:
        file.write(href.get('href') + '\n')
    file.close()


if __name__ == '__main__':
    get_chapter_links(
        'https://mintmanga.live/mag_celitel__novyi_start___vysshee_iscelenie__chary_momentalnoi_smerti_i_kraja_umenii')
