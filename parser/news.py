import requests
from bs4 import BeautifulSoup

URL = 'https://kaktus.media/?lable=8&date=2023-01-30&order=time'

HEADERS = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                     "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
           }


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    data = BeautifulSoup(html.text, 'html.parser')
    items = data.find_all("div", class_="ArticleItem--data ArticleItem--data--withImage")
    all_news = []

    for item in items:
        news = {
            'link':  item.find('a').get('href'),
            'time': item.find('div', 'ArticleItem--time').string.replace('\n', '')
        }
        all_news.append(news)
    return all_news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        html = get_html(URL)
        new = get_data(html)
        news.extend(new)

        return news
    else:
        raise Exception("Error in parser!")
