from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def get_driver():
#Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def get_temp(temp):
    """Extracting temp value only"""
    try:
        element = float(temp[-2:])
    except:
        print("Increase time.sleep(s)")
    return element

def obtain_values(header, temp):
    driver = get_driver()
    time.sleep(3)
    element_header = driver.find_element(By.XPATH, header)
    element_temp = driver.find_element(By.XPATH, temp)
    return (element_header.text, get_temp(element_temp.text))

scraped_values = obtain_values("/html/body/div[1]/div/h1[1]", "/html/body/div[1]/div/h1[2]")


print(f"header: {scraped_values[0]} \nworld temperature: {scraped_values[1]}")
