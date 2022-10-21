from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrom_driver_path="C:\devlepment\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrom_driver_path)
driver.get("https://tinder.com/")
time.sleep(5)
login=driver.find_element(By.LINK_TEXT,'Log in')
login.click()
time.sleep(2)
more=driver.find_element(By.LINK_TEXT,"MORE OPTIONS")
more.click()
time.sleep(5)
facebook=driver.find_element(By.LINK_TEXT,"LOG IN WITH FACEBOOK")
facebook.click()