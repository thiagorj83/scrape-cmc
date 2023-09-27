

def browser_get(browser,url):
    try:
        browser.get(url)

        browser.maximize_window()
    except Exception as e:
        print(f"Ocorreu o erro: {e}")