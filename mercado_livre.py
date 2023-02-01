import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

url_base = "https://lista.mercadolivre.com.br/"
product = input('Product name?')
pages = int(input('Number of pages you want to search?'))

options = Options()
options.add_argument("--headless")
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get(url_base + product)

for page in range(pages):
    items = browser.find_elements(By.CLASS_NAME, 'andes-card')
    for item in items:
        
        item_title = item.find_element(By.TAG_NAME,'h2').text
        item_link = item.find_element(By.TAG_NAME,'a').get_attribute('href')
        
        
        items_price_length = len(item.find_elements(By.CLASS_NAME,'price-tag-fraction'))


        if items_price_length == 3:
            item_price_real = item.find_elements(By.CLASS_NAME,'price-tag-fraction')[1].text
            item_price_cents = item.find_elements(By.CLASS_NAME,'price-tag-cents')[1].text
        elif items_price_length == 2:
            item_price_real = item.find_element(By.CLASS_NAME,'price-tag-fraction').text
            item_price_cents = item.find_element(By.CLASS_NAME,'price-tag-cents').text
            
        item_price = ''


        if item_price_cents:
            item_price = f'{item_price_real},{item_price_cents}'
        else:
            item_price = item_price_real

        
        print(item_title)
        print(item_link)
        print(item_price)
        print("\n\n")


    print(f'Page: {page+1}')
    print('===============================================')
    
    try:
        cookies = browser.find_element(By.CLASS_NAME,'cookie-consent-banner-opt-out__action')
        cookies.click()
    except:
        pass

    next_page = browser.find_element(By.CLASS_NAME,'shops__pagination-link')
    sleep(1.5)
    
    if page + 1 < pages:
        next_page.click()
        sleep(1.5)

    

    
    




