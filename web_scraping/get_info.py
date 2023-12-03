from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_temp(temp):
    #extract temp value
    try:
        element = float(temp[-2:])
    except ValueError as e:
        print("Error extracting temperature: ", e)
        print("Increase time.sleep(s)")
    return element

def obtain_values(driver, header, temp):
    time.sleep(3)
    element_header = driver.find_element(By.XPATH, header)
    element_temp = driver.find_element(By.XPATH, temp)
    result = (element_header.text, get_temp(element_temp.text))
    return result