# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны​

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import matplotlib.pyplot as plt
import numpy as np


def get_prices_from_current_page(dr):
    prices = []
    for span in dr.find_elements(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH"):
        prices.append(int(span.text.replace('руб.', '').replace(' ', '')))
    return prices


driver = webdriver.Chrome()

url = "https://www.divan.ru/category/divany-i-kresla?types%5B%5D=1&types%5B%5D=4&types%5B%5D=54"

driver.get(url)

time.sleep(5)

parsed_data = []

parsed_data.extend(get_prices_from_current_page(driver))

# print(parsed_data)
# print(length = {len(parsed_data)}')

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(parsed_data)

print(f'mean = {np.mean(parsed_data)}')

plt.hist(parsed_data, 7)
plt.xlabel('Divan price')
plt.ylabel('Frequency')
plt.title('Histogram of divan prices')
plt.show()

# while True:
#     next_page = driver.find_element(By.CSS_SELECTOR, "a.ui-LD-6h")