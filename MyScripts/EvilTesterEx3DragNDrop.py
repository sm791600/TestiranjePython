from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://testpages.eviltester.com/pages/interaction/drag-drop/")

draggableElement = driver.find_element(By.ID, "draggable1")
droppableElement = driver.find_element(By.ID, "droppable1")
draggableElement2 = driver.find_element(By.ID, "draggable2")
droppableElement2 = driver.find_element(By.ID, "droppable2")

sleep(3)
dragAction = ActionChains(driver)
dragAction.drag_and_drop(draggableElement, droppableElement).perform()
sleep(3)

dragAction = ActionChains(driver)
dragAction.drag_and_drop(draggableElement2, droppableElement2).perform()
sleep(5)

sleep(8)
driver.quit()