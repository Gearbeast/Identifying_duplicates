import requests
from bs4 import BeautifulSoup

import links
import parser_perricone


def main():
    page_link_list = links.get_page_links()
    for page_link in page_link_list:
        # print(page_link)
        prod_link_list = links.get_product_links( links.get_html(page_link) )
    print(links.link_list)



if __name__ == '__main__':
    main()