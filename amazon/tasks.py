import logging

import requests
from bs4 import BeautifulSoup
from celery import shared_task
from requests.exceptions import RequestException

from amazon.models import Product, Brand

logger = logging.getLogger(__name__)


class AmazonAppleScraper:

    base_url = "https://www.amazon.co.uk"
    store_url = "https://www.amazon.co.uk/stores/page/B49C58BF-1F41-4220-8249-B43BD19F919C"

    def __init__(self):
        self.products = []

    def scrape_store(self):
        try:
            response = requests.get(self.store_url)
            response.raise_for_status()
        except RequestException as e:
            logger.error(f"Failed to retrieve the store page: {e}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        product_elements = soup.find_all('li', {'class': 'ProductGridItem__itemOuter__KUtvv'})

        for product in product_elements:
            product_link = product.find('a', {'class': 'Overlay__overlay__LloCU'})

            if product_link:
                link = product_link['href']
                product_url = f'{self.base_url}{link}'

                try:
                    brand, created = Brand.objects.get_or_create(name='Apple')
                    product_details = self.scrape_product_details(product_url, brand)
                    if product_details:
                        self.products.append(product_details)
                except Exception as e:
                    logger.error(f"Error scraping product details from {product_url}: {e}")

        return self.products

    def scrape_product_details(self, product_url, brand):
        try:
            response = requests.get(product_url)
            response.raise_for_status()
        except RequestException as e:
            logger.error(f"Failed to retrieve product page {product_url}: {e}")
            return {}

        soup = BeautifulSoup(response.content, 'html.parser')
        product_data = {
            'name': self.get_product_name(soup),
            'sku': self.get_product_sku(soup),
            'asin': self.get_product_asin(soup),
            'image': self.get_product_image(soup),
            'instructions': self.get_product_instructions(soup)
        }

        if product_data['name'] and product_data['asin']:
            try:
                Product.objects.get_or_create(
                    brand=brand,
                    name=product_data['name'],
                    asin=product_data['asin'],
                    defaults=product_data
                )
            except Exception as e:
                logger.error(f"Error saving product to database: {e}")

        return product_data

    def get_product_name(self, soup):
        title_element = soup.find(id='productTitle')
        return title_element.get_text(strip=True) if title_element else None

    def get_product_sku(self, soup):
        sku_element = soup.find('span', {'class': 'sku'})
        return sku_element.get_text(strip=True) if sku_element else None

    def get_product_asin(self, soup):
        asin_element = soup.find('input', {'id': 'ASIN'})
        return asin_element['value'] if asin_element else None

    def get_product_image(self, soup):
        image_element = soup.find('img', {'id': 'landingImage'})
        return image_element['src'] if image_element else None

    def get_product_instructions(self, soup):
        instructions_element = soup.find('div', {'id': 'productDescription'})
        return instructions_element.get_text(strip=True) if instructions_element else None


@shared_task
def scrape_amazon():
    scraper = AmazonAppleScraper()
    return scraper.scrape_store()
