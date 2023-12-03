import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def read_credentials():
    config = configparser.ConfigParser()
    config.read("config.ini")

    username = config.get("Credentials", "username")
    password = config.get("Credentials", "password")
    return username, password

def user_login(driver, link):
    try:
        #detect element first
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_username")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_password")))

        #enter credentials
        username, password = read_credentials()
        driver.find_element(By.ID, "id_username").send_keys(username)
        driver.find_element(By.ID, "id_password").send_keys(password + Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.url_changes(link))

    except NoSuchElementException:
        print("Login form elements not found.")
    except TimeoutException:
        print("Login timed out")
    except ValueError as e:
        Print("Error logging in: ", e)

def return_to_home(driver):
    #return to homepage
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div/a")))
    element.click()