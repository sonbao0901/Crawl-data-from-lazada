from selenium import webdriver
import os
import time
import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
if __name__ == '__main__':
    data_df = []

    url_file_driver = os.path.join('etc', 'chromedriver.exe')
    service = Service(executable_path =url_file_driver)
    options = webdriver.ChromeOptions()
    
    driver = webdriver.Chrome(options=options, service=service)
    driver.get('https://covid19.gov.vn/')
    
    driver.switch_to.frame(1) #di chuyen toi frame can cao du lieu
    target = driver.find_elements(By.XPATH, "/html/body/div[2]/div[1]/div") #paste xpath cua du lieu can cao
    #dung loop for de lay du lieu
    for data in target:
        cities = data.find_elements(By.CLASS_NAME, "city")
        totals = data.find_elements(By.CLASS_NAME, "total")
        today = data.find_elements(By.CLASS_NAME, "daynow")
        dies = data.find_elements(By.CLASS_NAME, "die")

    list_cities = [city.text for city in cities]
    list_totals = [city.text for city in totals]    
    list_today = [city.text for city in today]
    list_dies = [city.text for city in dies]
    

    
    for i in range(len(list_cities)):
        row = '{}, {}, {}, {}\n'.format(list_cities[i],list_totals[i],list_today[i],list_dies[i])
        data_df.append(row)

    today_ = (datetime.datetime.now()).strftime("%Y%m%d")
    filename = f"{today_}.csv"
    with open(os.path.join(r'C:\Users\phanb\OneDrive\Máy tính\crawl\data', filename), 'w+', encoding='utf-8') as f:
        f.writelines(data_df)
    
    driver.close()
