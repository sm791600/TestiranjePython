import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
# импортираме библиотеки за користење sleep командата за паузирање на програмата,
#самиот webdriver, By овозможува селекција на елементи од веб страната

#ПРОВЕРИ ГИ КОМЕНТАРИТЕ ДАЛИ СЕ ТОЧНИ

driver = webdriver.Chrome()
#активира инстанца од Chrome која е под контрола на selenium

driver.get("https://testpages.eviltester.com/pages/basics/basic-web-page/")
driver.find_element(By.ID, "button1").click()

time.sleep(8)
driver.quit()
#driver. quit izgldea kako da e opcionalen bidejki se gasi i vaka i taka