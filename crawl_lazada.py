import numpy as np
from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
from time import sleep
import datetime
import pandas as pd

url_file_driver = os.path.join('etc', 'chromedriver.exe')

service = Service(executable_path=url_file_driver)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options= options, service=service)
driver.get("https://www.lazada.vn/dien-thoai-di-dong/?spm=a2o4n.home.cate_1.1.19053bdcuPAbP6")
sleep(random.randint(5, 10))



elems = driver.find_elements(By.CSS_SELECTOR, '.RfADt [href]')
title = [elem.text for elem in elems]
link = [elem.get_attribute('href') for elem in elems]

elem_price = driver.find_elements(By.CSS_SELECTOR, '.aBrP0')
price = [price.text for price in elem_price]

df1 = pd.DataFrame(list(zip(title, price,link)), columns= ['title', 'price', 'item_link'])
df1['index_'] = np.arange(1, len(df1)+1)

df1

elems_discount = driver.find_elements(By.CSS_SELECTOR, ".WNoq3")
discount = [discount.text for discount in elems_discount]


"""/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[4]/span
/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[4]/span"""
discount_list = []
for i in range(1, len(title)+1):
    try:
        discount = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[{}]/div/div/div[2]/div[4]/span".format(i))
        discount_list.append(discount.text)
    except NoSuchElementException:
        print("NoSuchElementException" + str(i))
        discount_list.append(np.nan)

len(discount_list)

index = [i for i in range(1,41)]

df2 = pd.DataFrame(list(zip(index,discount_list)), columns=['index','discount'])

df3 =df1.merge(df2, how = 'left', left_on='index_', right_on='index')

df3

df3.columns
df3.drop(columns=['index_', 'index'], inplace = True)

df3.info()                 


elem_city = driver.find_elements(By.CSS_SELECTOR, '._6uN7R')
city = [city.text for city in elem_city]

len(city)

df3['city'] = city

df3


driver.get(df3['item_link'][0])