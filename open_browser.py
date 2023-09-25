from selenium import webdriver

def open_browser():
    try:

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--disable-web-security')  # Desativa a segurança do CORS
        # chrome_options.add_argument("--headless")
        # browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",chrome_options=chrome_options)

        browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        return browser
    except Exception as e:
        print(f'Ocorreu o erro:{e}')