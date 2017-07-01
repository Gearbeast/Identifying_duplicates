import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        # print(result.text)
        return result.text
    except requests.exceptions.RequestException:
        print('Error')
        return False


def parse(html):
    
    with open("sample.log", 'a', encoding='utf-8') as sample:
        logging.basicConfig(filename="sample.log", level=logging.INFO)
        log = logging.getLogger("ex")

        product_id=product_name=product_price=product_description=product_details=key_sciences=ingredients=application=''

        try:
            soup = BeautifulSoup(html, 'html.parser')
            product_id = soup.find('header', class_="product-header product-section").find('span').text.strip()
            product_name = soup.find('div', class_='pdp-main').find('h1').text.strip()
            product_price = soup.find('div', class_='pdp-main').find('span', class_='sale--price').text.strip()
            product_description = soup.find('div', id='views').find('div', class_='product-description').text.strip()
            product_details = soup.find('div', id='tab1').text.strip()
            ingredients = soup.find('div', id='tab3').text.strip()
            application = soup.find('div', id='tab4').text.strip()
            key_sciences = soup.find('div', id='tab2').text.strip()
        
            # print(product_id)
            # print(product_name)
            # print(product_price)
            # print(product_description)
            # print(product_details)
            # print(key_sciences)
            # print(ingredients)
            # print(type(application))



        except Exception:
            log.exception("Error!")

    
   
    return product_id, product_name, product_price, product_description, product_details, key_sciences, ingredients, application
        


def main():
    url = 'http://www.perriconemd.com/skincare/exfoliators-toners/serum-prep-MP0074.html'
    html = parse( get_html(url) )

   
if __name__ == '__main__':
    main()