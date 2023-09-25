import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def scroll2element(by_,target,browser):

    timeout = 10
    found = False
    last_position=-1
    current_position=0
    while not found or last_position == current_position:
        try:
            element_present = EC.presence_of_element_located((by_,target))
            element = WebDriverWait(browser, timeout).until(element_present)
            is_in_viewport = browser.execute_script("""
                let rect = arguments[0].getBoundingClientRect();
                let windowHeight = (window.innerHeight || document.documentElement.clientHeight);
                let windowWidth = (window.innerWidth || document.documentElement.clientWidth);
                return (
                    rect.top >= 0 &&
                    rect.left >= 0 &&
                    rect.bottom <= windowHeight &&
                    rect.right <= windowWidth
                );
            """, element)
            current_position = browser.execute_script("return window.pageYOffset;")

            if is_in_viewport  or last_position == current_position:
                found = True
                
                click_item=browser.find_element(by_,target)

                click_item.click()
                time.sleep(5)
                scroll2element(by_,target,browser)
                return True

            else:
                last_position=current_position
                browser.execute_script("window.scrollBy(0, window.innerHeight);")
                current_position = browser.execute_script("return window.pageYOffset;")
        except TimeoutException:
                print("O elemento não pôde ser encontrado dentro do tempo limite.")
        
        finally:
                current_position = browser.execute_script("return window.pageYOffset;")
                scroll_height = browser.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
                browser.execute_script(f"window.scrollBy(0,{scroll_height});")
                last_position=browser.execute_script("return window.pageYOffset;")
                if last_position == current_position:
                    break 