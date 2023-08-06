from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import shutil
from selenium.webdriver.chrome.service import Service

driver= webdriver.Chrome()

driver.get(r'https://www.google.com/maps/@12.9662976,77.5847936,12z?entry=ttu')
driver.maximize_window()
time.sleep(2)


def searchplace():
    place=driver.find_element(By.XPATH,'//input[@id="searchboxinput"]')
    place.send_keys('rajajinagar')
    time.sleep(2)
    submit=driver.find_element(By.XPATH,'//button[@id="searchbox-searchbutton"]')
    submit.click()
    time.sleep(12)
searchplace()

img=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/button/img')
src=img.get_attribute('src')
time.sleep(2)
url =src
print(src)
response = requests.get(url,stream=True)
with open('img.png','wb') as out_file:
    shutil.copyfileobj(response.raw,out_file)
del response

def directions():
    time.sleep(10)
    directions=driver.find_element(By.XPATH,'/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button')
    directions.click()
directions()

def find():
    time.sleep(10)
    find=driver.find_element(By.XPATH,'//*[@id="sb_ifc50"]//input ').send_keys('sanjaynagar')
    time.sleep(3)
    search=driver.find_element(By.XPATH,'//*[@id="directions-searchbox-0"]/button[1]')
    search.click()

find()

def kilometers():
    time.sleep(3)
    totalkilometers= driver.find_element(By.XPATH,'//*[@id="section-directions-trip-1"]/div[1]/div/div[1]/div[2]/div')
    print('totalkilometers:',totalkilometers.text)
    totaltime= driver.find_element(By.XPATH,'//*[@id="section-directions-trip-1"]/div[1]/div/div[1]/div[1]')
    print('totaltime:',totaltime.text)
    time.sleep(2)
    bus=driver.find_element(By.XPATH,'//div[@jsnamespace="directions"]/div/div/div/div/div[4]/button/img').click()
    time.sleep(2)
    amount_in_bus=driver.find_element(By.XPATH,'//*[@id="section-directions-trip-0"]/div[1]/div/div[3]/span[1]')
    print('total amount in bus:',amount_in_bus.text)
    taotal_time_taken_in_bus=driver.find_element(By.XPATH,'//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div')
    print('total time taken in bus:',taotal_time_taken_in_bus.text)
kilometers()
time.sleep(2)
driver.close()