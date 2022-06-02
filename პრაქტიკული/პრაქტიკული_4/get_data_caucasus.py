import shutil
from typing import List
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


country_url = []
base = 'http://www.heraldika.ge/'

base_url = 'http://www.heraldika.ge/index.php?m=85&p_news=1'


def get_link(url, data):
    content = requests.get(url).text
    bs: BeautifulSoup = BeautifulSoup(content, 'html.parser')
    next_url: List[Tag] = bs.find(attrs={"class": 'armsslide'}).find_all('a')
    for a in next_url:
        data.append(urljoin(url, a.attrs['href']))
    for country in data:
        content = requests.get(country).text
        bs: BeautifulSoup = BeautifulSoup(content, 'html.parser')
        name = bs.find("meta",  property="og:title")['content']
        a=1
        print(bs.find(attrs={"class": 'armstxt'}).find_all('img'))


        for img in bs.find(attrs={"class": 'armstxt'}).find_all('img'):
           if a%2 == 1:
            res = requests.get(urljoin(base, img.get('src')), stream=True)
            with open(f"{name}_gerbi", 'wb') as f:
                shutil.copyfileobj(res.raw, f)
        else:
            res = requests.get(urljoin(base, img.get('src')), stream=True)
            with open(f"{name}_drosha", 'wb') as f:
                shutil.copyfileobj(res.raw, f)


scrape(base_url, country_url)
print(country_url)
