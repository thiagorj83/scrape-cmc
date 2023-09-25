from detect_element import detect_element
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def dismiss_cookie_banner(browser):

    banner_id = By.ID
    banner_element = 'onetrust-reject-all-handler'
    banner_msg = 'timeout na detecção do banner'
    browser.execute_script(f"window.scrollBy(0,100);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
    time.sleep(1)

    try:
        load_failed = detect_element(banner_id, browser, banner_element, banner_msg, 10)
        
        if not load_failed:
            banner = browser.find_element(banner_id, banner_element)
            banner.click()
    except NoSuchElementException:
        # Lida com o caso em que o elemento não é encontrado
        print("O elemento banner do cookie não foi encontrado.")
