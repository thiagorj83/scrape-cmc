import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def scroll2element(by_,target,browser):

    timeout = 10
    current_position=0
    finished=False
    last_position=0

    while not finished or current_position == last_position :
        try:
            element_present = EC.presence_of_element_located((by_,target))
            element = WebDriverWait(browser, timeout).until(element_present)
            last_position=browser.execute_script("return window.pageYOffset;")

            if element.is_displayed() and not finished:
                
                click_item=browser.find_element(by_,target)
                click_item.click()
                current_position = browser.execute_script("return window.pageYOffset;")
                time.sleep(1)

            if current_position == last_position and not element.is_displayed():
                finished=True                
                

        except Exception as e:
            print(e)
            break
            
        finally:
            scroll_height = browser.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
            browser.execute_script(f"window.scrollBy(0,{scroll_height});")

