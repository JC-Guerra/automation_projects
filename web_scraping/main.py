from selenium import webdriver
import get_info

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

    driver = webdriver.Chrome(options=options)
    driver.get(link)
    return driver

def main():
    link = "https://automated.pythonanywhere.com/"
    driver = get_driver(link)

    header_xpath = "/html/body/div[1]/div/h1[1]"
    temp_xpath = "/html/body/div[1]/div/h1[2]"
    scraped_values = get_info.obtain_values(driver, header_xpath, temp_xpath)
    print(f"header: {scraped_values[0]} \nworld temperature: {scraped_values[1]}")

    driver.quit()

if __name__ == "__main__":
    main()