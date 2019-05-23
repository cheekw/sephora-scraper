from bs4 import BeautifulSoup
import requests
import re

def get_html(url):
	sephora_page = ''
	while sephora_page == '':
		try:
			sephora_page = requests.get(url)
			break
		except:
			print("Connection refused by the server..")
			print("Sleeping for 5 seconds")
			time.sleep(5)
			continue
	return BeautifulSoup(sephora_page.content, 'lxml')

def find_num_pages(sephora_html):
	num_products = sephora_html.find('span', {'data-at': 'number_of_products'}).get_text()
	num_products = int(re.findall('^\D*(\d+)', num_products)[0])
	return round(num_products / 60)

def find_product_urls(sephora_html): 
	script_string = sephora_html.find_all('script', {'type' : 'application/ld+json'})[1].get_text()
	return re.findall('(?<="url":").*?(?=\")', script_string)

