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
    soup = BeautifulSoup(html, 'html.parser')
    product_id = soup.find('header', class_="product-header product-section").find('span').text.strip()
    product_name = soup.find('div', class_='pdp-main').find('h1').text.strip()
    product_price = soup.find('div', class_='pdp-main').find('span', class_='product--sale').find('span').nextSibling.text.strip()
    product_description = soup.find('div', id='views').find('div', class_='product-description').text.strip()
    product_details = soup.find('div', id='tab1')
    key_sciences = soup.find('div', id='tab2')
    ingredients = soup.find('div', id='tab3')
    application = soup.find('div', id='tab4')

    print(product_id)
    print(product_name)
    print(product_price)
    print(product_description)
    print(product_details)
    print(key_sciences)
    print(ingredients)
    print(application)
   
        

    # product_details = soup.find('div', id='tab1').contents[0].strip() contents[1] ???


    # details = {}
    # for i in product_details:
    #     if i == 
    #     details = details.append(i)
    #     print(details)




    # projects = []
    
    # for row in product_name:
    #      cols = row.find('h1')
    #      projects.append(cols)

    # return projects     

    
        
        # projects.append({
        #     'title': cols[0].a.text
            #'numbers': [number.text for number in cols[0].div.find_all('container cleared')]

        # })

    # for project in projects:
    #     print(project)





def main():
    url = 'http://www.perriconemd.com/skincare/exfoliators-toners/serum-prep-MP0074.html'
    html = parse( get_html(url) )

   


if __name__ == '__main__':
    main()