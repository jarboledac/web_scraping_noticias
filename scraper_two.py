import requests
from bs4 import  BeautifulSoup
#import lxml.html as html


URL_NEW = "https://www.qhubomedellin.com/categoria/ultimas-noticias/"




def page_links(url):
    request_url = requests.get(url)
    if request_url.status_code == 200:
        page_url = BeautifulSoup(request_url.text, "html.parser")
        articles = page_url.find('div', attrs={"class": "mh-loop mh-content"}).find_all("article")
        for art_links in articles:
            print(art_links.a.get("href"))
    else:
        raise ValueError(f'Error: {request_url.status_code}')



if __name__ == '__main__':
    page_links(URL_NEW)