from numpy import random
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
import time

df = pd.read_csv("urls_data.csv")

asin_column = df['ASIN']


def conc_url(asin):
    return asin


asin_all = asin_column.apply(lambda x: conc_url(x)).tolist()

# asins = asin_all[0:15]
asins = asin_all[25:40]

# asins = asin_all

ASIN = 'B082DK316V'


def pram_maker(ASIN):
    return '{%s}' % (f'"asin":"{ASIN}"')


def initialize(driver):

    driver.get('https://www.amazon.com/s?k=B08RNKTFXY&ref=nb_sb_noss')

    loc = driver.find_element(By.XPATH,
                              '//*[@id="nav-global-location-popover-link"]')
    loc.click()

    try:
        loc_zip = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="GLUXZipUpdateInput"]')))
    finally:
        print("No Element")

    loc_zip.click()
    loc_zip.send_keys("10001")
    driver.find_element(By.XPATH,
                        '//*[@id="GLUXZipUpdate"]/span/input').click()
    try:
        driver.find_element(
            By.XPATH, '//*[@id="a-popover-2"]/div/div[2]/span/span').click()
        driver.find_element(
            By.XPATH, '//*[@id="a-popover-2"]/div/div[2]/span/span').click()
    except:
        print("Something Went Wrong!")
    return driver


def new_tab_url(ASIN, driver):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 'w')
    driver.get(f'https://www.amazon.com/s?k={ASIN}&ref=nb_sb_noss')


def get_coupon(page_source, ASIN):
    soup = BeautifulSoup(page_source, 'html.parser')
    span = soup.find_all('span', {'data-component-props': pram_maker(ASIN)})
    try:
        coupon_amount = span[0].find('span', {
            'class': 's-coupon-highlight-color'
        }).text.strip()
        coupon_amount = coupon_amount.split(' ', -1)
        return coupon_amount[1]
    except IndexError as e:
        print(f'{e}: Coupon Does Not Exist for ASIN: {ASIN}')
        return "Nill"


def main():

    driver = webdriver.Edge()
    # Basic Setup for the Amazon.com (Change Address etc)
    initialize(driver)
    time.sleep(5)
    # List to store the ASIN base URL and coupon amount
    coupons = []
    # Open a new tab and go to the next ASIN in user ASIN file
    for asin in asins:
        new_tab_url(asin, driver)
        time.sleep(random.randint(1))
        page_source = driver.page_source
        coupon_amount = get_coupon(page_source, asin)
        coupons.append({
            "URL": f'https://www.amazon.com/s?k={asin}&ref=nb_sb_noss',
            "Coupon": coupon_amount
        })

    # Scraping Completion Prompt
    print(
        "Finished Scraping! You can see the coupons in the Coupons.csv file.")
    # Convert and Save the Scraped Data to CSV format
    res = pd.DataFrame(coupons)
    res.to_csv("Coupons.csv", index=False)
    time.sleep(60)
    # Close the Edge Browser
    driver.quit()


if __name__ == "__main__":
    main()
