import csv
import requests
from bs4 import BeautifulSoup

import links
import parser_perricone

# def get_data:
#     pass


# def write_csv:
#     pass
    # with open("perricone.csv", 'a', encoding='utf-8') as perricone:
    #     perricone.write()


def main():

    with open("data_soup.csv", 'a', encoding='utf-8') as data_soup:
        fields = ['product_id', 'product_name', 'product_price', 'product_description', 'product_details', 'key_sciences', 'ingredients', 'application']
        writer = csv.DictWriter(data_soup, fields, delimiter=';')
        writer.writeheader()

        all_links = []
        page_link_list = links.get_page_links()
        for page_link in page_link_list:
            # print(page_link)
            all_links += links.get_product_links( links.get_html(page_link) )
            #if len(prod_link_list) > 0:
            # all_links += prod_link_list
        # print(all_links)

        for link in all_links:
            print(link)
            text_product = parser_perricone.parse( parser_perricone.get_html(link) )
            # print(text_product)

        return text_product

        for row_text in text_product:
            print(row_text)
            print(type(row_text))
            writer.writerow(row_text)


if __name__ == '__main__':
    main()