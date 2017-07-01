import requests
from bs4 import BeautifulSoup

import crawler


def get_html(page_link):
    r = requests.get(page_link)
    return r.text


def get_product_links(html):
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.find_all('div', class_="grid-tile ")
    # print(products)
    i = 0
    link_list = []
    for product in products:
        # print(product)
        product_name = product.find_all('div', class_="product-name")
        #print(product_name)
        for a in product_name:
            b = a.find('a').get('href')
            #print(b)
            link = 'https://www.perriconemd.com' + b
            #print(type(link))
            i += 1
            link_list.append(link)
    # i += i        
    # print(i)

    # print(link_list)
    return link_list
  

def get_page_links():

# переделать! url должен принимать из crawler.py ссылки на категории.
# Строка x = 'https://www.perriconemd.com/skincare/shop-by-concern/?sz=12&start=' + i + '&format=page-element'
# должна выглядеть x = (элемент из url) + (a = '?sz=12&start=') + i + (b = '&format=page-element')
    
    shop_by_product = 'https://www.perriconemd.com/skincare/shop-by-product'
    shop_by_collection = 'https://www.perriconemd.com/skincare/shop-by-collection'
    shop_by_concern = 'https://www.perriconemd.com/skincare/shop-by-concern'
    value_sets = 'https://www.perriconemd.com/skincare-sets/'
    supplements = 'https://www.perriconemd.com/supplements-shop-all/'
    basis_link = [shop_by_product, shop_by_collection, shop_by_concern, value_sets, supplements]
    urls = []

    for i in range(12, 96, 12):
        i = str(i)
        #print(type(i))
        x = '%s/?sz=12&start=%s&format=page-element' % (shop_by_product, i)
        urls.append(x)
        y = '%s/?sz=12&start=%s&format=page-element' % (shop_by_collection, i) 
        urls.append(y)
        z = '%s/?sz=12&start=%s&format=page-element' % (shop_by_concern, i)
        urls.append(z)
    
    for l in basis_link:
        urls.append(l)
    #print(urls)
    return urls

def main():
    page_link_list = get_page_links()
    for page_link in page_link_list:
        # print(page_link)
        prod_link_list = get_product_links( get_html(page_link) )
    #print(link_list)
    # Заготовка
    # url = 'https://www.perriconemd.com/skincare/shop-by-product/'
    # links = crawler.get_shop_by_links( crawler.get_html(url) )
    # for ls in links:
    #     prod_link_list = get_product_links( get_html(page_link) )


if __name__ == '__main__':
    main()