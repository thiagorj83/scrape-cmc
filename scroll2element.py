import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def scroll2element(by_,target,browser):

    timeout = 10
    found = False
    current_position=0
    is_visible=False
    finished=False
    last_position=0

    while not finished or current_position == last_position :
        try:
            found=False
            element_present = EC.presence_of_element_located((by_,target))
            element = WebDriverWait(browser, timeout).until(element_present)
            last_position=browser.execute_script("return window.pageYOffset;")
            print('*****************')
            print(f'current_position:{current_position}')
            print(f'last_position:{last_position}')
            print(f'finished:{finished}')
            print(f'element displayed:{element.is_displayed()}')
            print('*****************')
            if element.is_displayed() and not finished:
                found = True
                print('found')
                
                click_item=browser.find_element(by_,target)
                click_item.click()
                current_position = browser.execute_script("return window.pageYOffset;")
                time.sleep(1)

            if current_position == last_position and not element.is_displayed():
                finished=True
                print('finished')
                
                

        except Exception as e:
            print(e)
            break
            
        finally:
            print('finally')  
            scroll_height = browser.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
            browser.execute_script(f"window.scrollBy(0,{scroll_height});")

