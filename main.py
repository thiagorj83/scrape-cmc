from open_browser import open_browser
from call_cmc_api import call_cmc_api
from scroll2element import scroll2element
from dismiss_cookie_banner import dismiss_cookie_banner
from datetime import datetime
import os
from selenium.webdriver.common.by import By
from browser_get import browser_get
import csv
import time



OUTPUT_FILE = 'cmc_coin_data.csv'
current_directory = os.getcwd()
# Caminho completo para o arquivo de saída
output_path = os.path.join(current_directory, OUTPUT_FILE)

OUTPUT_FILE2 = 'coinmarketcap.html'
output_path2 = os.path.join(current_directory, OUTPUT_FILE2)

def main():
    
    start_time=datetime.now()
    print(f'start time:{start_time}')

    browser=open_browser()
    browser_get(browser,'https://coinmarketcap.com/all/views/all/')
    
    dismiss_cookie_banner(browser)

    html = browser.page_source



    # Salva o HTML em um arquivo local
    with open(output_path2, 'w', encoding='utf-8') as file:
        file.write(html)
    
    
    target='//*[@id="__next"]/div[2]/div[2]/div/div[1]/div/div[3]/button'
    
    while scroll2element(By.XPATH,target,browser):
        scroll2element(By.XPATH,target,browser)

    rank=browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr[last()]/td[1]/div').text

    time.sleep(3)
    if int(rank) > 9000:
        cmc_data=call_cmc_api(rank)
        if len(cmc_data) > 0:
            with open(output_path, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(cmc_data)

    else:
        print('A página não foi raspada corretamente.')
    print(f'Total lines:{rank}')

    finish_time=datetime.now()
    print(f'Finish time:{finish_time}')
    elapsed_time = finish_time - start_time
    print(f'Elapsed time:{elapsed_time}')

if __name__=="__main__":

    main()
