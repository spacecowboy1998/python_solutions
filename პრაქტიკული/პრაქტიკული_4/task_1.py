import shutil
from typing import List
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class CaucasusData:
    def __init__(self, base, url_link, cnt_data):
        self.base = base
        self.url = url_link
        self.data = cnt_data

    def get_country_link(self):
        content = requests.get(self.url).text
        bs: BeautifulSoup = BeautifulSoup(content, 'html.parser')
        next_url: List[Tag] = bs.find(attrs={"class": 'armsslide'}).find_all('a')
        for a in next_url:
            self.data.append(urljoin(self.url, a.attrs['href']))
        return self.data

    def get_images(self):
        for country_link in self.get_country_link():
            content = requests.get(country_link).text
            bs: BeautifulSoup = BeautifulSoup(content, 'html.parser')
            name = bs.find("meta", property="og:title")['content']
            image_links = bs.find(attrs={"class": 'armstxt'}).find_all('img')
            res = requests.get(urljoin(self.base, image_links[0].get('src')), stream=True)
            with open(f"{name}_gerbi", 'wb') as f:
                shutil.copyfileobj(res.raw, f)

            res = requests.get(urljoin(self.base, image_links[1].get('src')), stream=True)
            with open(f"{name}_drosha", 'wb') as f:
                shutil.copyfileobj(res.raw, f)

    def get_names(self):
        names = []
        for country in self.get_country_link():
            content = requests.get(country).text
            bs: BeautifulSoup = BeautifulSoup(content, 'html.parser')
            names.append(bs.find("meta", property="og:title")['content'])
        return names


base_url = 'http://www.heraldika.ge/'
url = 'http://www.heraldika.ge/index.php?m=85&p_news=1'
info_data = []

data = CaucasusData(base_url, url, info_data)

print(data.get_names())
print(data.get_country_link())
print(data.get_images())
