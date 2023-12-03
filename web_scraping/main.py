from selenium import webdriver
from selenium.webdriver.common.by import By
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
        automated_login.go_to_contact_us(driver)

        css_selector = "#shopify-section-page-contact-us"
        contact_sc = driver.find_element(By.CSS_SELECTOR, css_selector)
        contact_sc.screenshot("contact_us_screenshot.png")

    finally:
        if driver is not None:
            driver.quit()
            print("Driver resources removed")

if __name__ == "__main__":
    link = link = "https://titan22.com/account/login?return_url=%2Faccount"
    main(link)