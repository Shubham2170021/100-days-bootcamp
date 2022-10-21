from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrom_driver_path="C:\devlepment\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrom_driver_path)
url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(url)
singin=driver.find_element(By.LINK_TEXT,"Sign in")
singin.click()
time.sleep(5)
user_id=driver.find_element(By.ID,"username")
user_id.send_keys("shubhamtripathia17@gmail.com")
password=driver.find_element(By.ID,"password")
password.send_keys("Shubham@10")
singin=driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
singin.click()
apply=driver.find_element(By.CSS_SELECTOR,'.jobs-apply-button')
apply.click()
next=driver.find_element(By.CSS_SELECTOR,".artdeco-button--primary")
next.click()
review=driver.find_element(By.CSS_SELECTOR,".artdeco-button--primary")
review.click()
submit_button=driver.find_element(By.CSS_SELECTOR,".artdeco-button--primary")
submit_button.click()
# artdeco-button--primary
# driver.find_element(By.TAG_NAME,"input")



