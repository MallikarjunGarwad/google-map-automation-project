from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

import time


import shutil
from selenium.webdriver.chrome.service import Service


driver=webdriver.Chrome()

driver.get(r'https://www.google.com/maps/place/Hebbal,+Bengaluru,+Karnataka/@13.0346428,77.5878734,15z/data=!4m6!3m5!1s0x3bae17a295d80a47:0x1a3ccbf328b14759!8m2!3d13.0353557!4d77.5987874!16zL20vMDZoNHJi?entry=ttu')
driver.maximize_window()
time.sleep(2)

img=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/button/img')
src=img.get_attribute('src')
time.sleep(2)
url =src
print(src)
response = requests.get(url,stream=True)
with open('img.png','wb') as out_file:
    shutil.copyfileobj(response.raw,out_file)
del response