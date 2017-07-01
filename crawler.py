import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_shop_by_links(html):

    soup = BeautifulSoup(html, 'html.parser')

    headings = soup.find('aside', id="secondary").find_all('h5')
    #print(headings)
    links_headings = []

    for heading in headings:
        a = heading.find('a')#.get('href')
        #print(a)
        if a is None:
            continue
        else:
            a = a.get('href')
            #print(a)
        link = 'https://www.perriconemd.com' + a
        #print(link)
        links_headings.append(link)
    print(links_headings)

    return links_headings



def main():
    url = 'https://www.perriconemd.com/skincare/shop-by-product/'
    links = get_shop_by_links( get_html(url) )

# перенести весь код в links.py
# На выходе должна получать еще ссылки:
# Основные товары - получает
# https://www.perriconemd.com/skincare/shop-by-product/
# https://www.perriconemd.com/skincare/shop-by-collection
# https://www.perriconemd.com/skincare/shop-by-concern

# Наборы
# https://www.perriconemd.com/skincare-sets/

# Добавки
# https://www.perriconemd.com/supplements-shop-all/


if __name__ == '__main__':
    main()