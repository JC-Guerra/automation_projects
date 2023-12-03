from selenium import webdriver
import time
import get_info
import automated_login
from datetime import datetime as dt
import save_file

#selenium update conflicts with other packages, run in virtual environment

def get_driver(link):
    #Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        return driver
    except ValueError as e:
        print("Webdriver error: ", e)
        
def main(link):

    driver = get_driver(link)

    try:
        automated_login.user_login(driver, link)
        print("Successfully logged in")
        automated_login.return_to_home(driver)

        header_xpath = "/html/body/div[1]/div/h1[1]"
        temp_xpath = "/html/body/div[1]/div/h1[2]"

        flag = 0
        while flag < 3:
            flag += 1
            header_value, temp_value = get_info.obtain_values(driver, header_xpath, temp_xpath)
            content = f"Header: {header_value} \nWorld temperature: {temp_value}"

            save_file.write_file(content)
            print(f"File has been written with the following: \n{content}")

    finally:
        if driver is not None:
            driver.quit()
            print("Driver resources removed")

if __name__ == "__main__":
    link = link = "https://automated.pythonanywhere.com/login"
    main(link)