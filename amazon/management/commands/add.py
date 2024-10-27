from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup

import time

class Command(BaseCommand):
    help = 'a'

    def handle(self, *args, **options):
        base_url = "https://www.amazon.co.uk"
        url = "https://www.amazon.co.uk/stores/page/B49C58BF-1F41-4220-8249-B43BD19F919C"
        print('Scraping Amazon iPhone store...')

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find product listings using the new class names
        product_elements = soup.find_all('li', {'class': 'ProductGridItem__itemOuter__KUtvv'})

        products = []
        for product in product_elements:

            product_link = product.find('a', {'class': 'Overlay__overlay__LloCU'})

            if product_link:

                link = product_link['href']
                product_url = f'{base_url}{link}'

                print(product_url)

                # Scrape product details
                product_details = self.scrape_product_details(product_url)
                products.append(product_details)

        return products

    def scrape_product_details(self, product_url):
        print(product_url)
        product_response = requests.get(product_url)
        product_soup = BeautifulSoup(product_response.content, 'html.parser')
        # print(product_soup)

        # Extracting product name
        name = product_soup.find(id='productTitle')
        # name = product_soup.find('span', {'class': 'a-size-large'})
        print(name)
        return True

        # Extracting product image URL
#         image = product_soup.find(id='imgTagWrapperId').find('img')['src']
#
#         # Extracting product description
#         description = product_soup.find(id='productDescription').get_text(strip=True)
#
#         print({
#             'name': name,
#             'image': image,
#             'description': description
#         }
# )
#
#         return {
#             'name': name,
#             'image': image,
#             'description': description
#         }


    def scrape_amazon_iphone_store(self, url):
        pass
        #
        #     if product_link:
        #         # Extract the href attribute
        #         link = product_link['href']
        #         product_url = f'https://www.amazon.com{link}'
        #
        #         # Scrape product details
        #         product_details = self.scrape_product_details(product_url)
        #         products.append(product_details)
        #
        # return products
