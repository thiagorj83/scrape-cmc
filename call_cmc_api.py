import requests


def call_cmc_api(rank):

        # URL da API
    url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

    # Parâmetros da consulta
    params = {
        "start": "1",
        "limit": f"{int(rank)}",
        "sortBy": "market_cap",
        "sortType": "desc",
        "convert": "USD",
        "cryptoType": "all",
        "tagType": "all",
        "audited": "false"
    }
    data=[]
    # Fazendo a requisição GET
    response = requests.get(url, params=params)
    # Verificando se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Convertendo a resposta para JSON
        data = response.json()
        # Agora você pode trabalhar com os dados JSON como desejar
        # Por exemplo, para imprimir os dados brutos:
    else:
        print(f"A requisição falhou com código de status {response.status_code}")

   
    cmc_coin_data=[]
    for i in range (0,len(data['data']['cryptoCurrencyList'])):
        cmc_coin_data.append([data['data']['cryptoCurrencyList'][i]['symbol'],data['data']['cryptoCurrencyList'][i]['slug']])
    
    return cmc_coin_data