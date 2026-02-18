from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    basket_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))
    assert basket_button.is_displayed()

    print(f"Текст кнопки: {basket_button.text}")
    