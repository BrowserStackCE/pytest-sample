import pytest
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('driver')
class TestLink:

    def test_bstackdemo(self, driver):
        driver.get("https://bstackdemo.com/")
        WebDriverWait(driver, 10).until(EC.title_contains("StackDemo"))
    # Get text of an product - iPhone 12
        item_on_page =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/p'))).text
    # Click the 'Add to cart' button if it is visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/div[4]'))).click()
    # Check if the Cart pane is visible
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart__content")))
    ## Get text of product in cart
        item_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))).text
        