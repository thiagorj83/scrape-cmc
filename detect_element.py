import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def detect_element(by_,browser,item,msg,tentativas):
    try:
        load_failed=False
        timeout=random.randint(10, 20)
        print(f'timeout:{timeout}')
        element_present = EC.presence_of_element_located((by_, item))
        WebDriverWait(browser, timeout).until(element_present)
    except :
        print(msg)
        load_failed=True

    while load_failed==True and tentativas > 0 :
        browser.refresh()
        timeout=random.randint(10, 20)

        time.sleep(timeout)
        try:
            element_present = EC.presence_of_element_located((by_, item))
            WebDriverWait(browser, timeout).until(element_present)
            
        except:
            if tentativas > 0:
                tentativas = tentativas - 1
                print(f'Tentando novamente...{timeout}')
            else:
                print(f'Todas as tentativas de carregamento da pagina falharam...{timeout}')
                exit()
        else:
            load_failed=False
    return load_failed