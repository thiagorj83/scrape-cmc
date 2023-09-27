import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def scroll2element2(by_, target, browser, max_attempts=5):
    timeout = 10
    attempts = 0

    while attempts < max_attempts:
        try:
            element_present = EC.presence_of_element_located((by_, target))
            element = WebDriverWait(browser, timeout).until(element_present)
            
            if element.is_displayed() and element.is_enabled():
                element.click()
                return True
            else:
                print("Element is not clickable.")
                return False
        except TimeoutException:
            print("O elemento não pôde ser encontrado dentro do tempo limite.")
        except Exception as e:
            print(f"Erro: {str(e)}")

        # Scroll down the page
        browser.execute_script("window.scrollBy(0, window.innerHeight);")
        attempts += 1

    print(f"Elemento '{target}' não encontrado após {max_attempts} tentativas.")
    return False

# Exemplo de uso:
# scroll_to_element_and_click(By.XPATH, "//button[@id='load-more-button']", browser)
