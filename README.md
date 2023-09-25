# CoinMarketCap Data Scraper

Este é um projeto simples que envolve a raspagem de dados do site CoinMarketCap usando Python e Selenium. O objetivo principal do projeto é extrair informações sobre criptomoedas da página CoinMarketCap e salvá-las em um arquivo CSV local.

## Funcionalidades

- Abre um navegador da web automaticamente.
- Navega até a página inicial do CoinMarketCap.
- Fecha automaticamente o banner de cookies.
- Salva o HTML da página inicial em um arquivo local.
- Rola a página até encontrar um elemento específico ( botão load more)
- Extrai a classificação (rank) da última criptomoeda listada.
- Verifica se o rank é superior a 9000.
- Se o rank for maior que 9000, faz uma chamada à API para obter dados adicionais da criptomoeda.
- Salva os dados da criptomoeda em um arquivo CSV local.

## Pré-requisitos

Antes de usar este projeto, certifique-se de ter os seguintes pré-requisitos instalados:

- Python
- Selenium
- Chrome WebDriver
- Uma conta no [CoinMarketCap](https://coinmarketcap.com/) (para obter uma chave de API, se necessário)

## Como Usar

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Certifique-se de ter configurado seu ambiente Python com as bibliotecas necessárias.

3. Execute o arquivo `main.py`:

   ```bash
   python main.py
   ```

4. O script abrirá um navegador, acessará o CoinMarketCap e realizará a raspagem de dados conforme descrito.

## Saída

Os dados da criptomoeda raspada serão salvos em um arquivo CSV local chamado `cmc_coin_data.csv`, e o HTML da página inicial do CoinMarketCap será salvo em `coinmarketcap.html`.

---

Este projeto é uma demonstração simples de como usar Python e Selenium para raspagem de dados na web. Sinta-se à vontade para adaptá-lo às suas necessidades específicas e expandi-lo conforme necessário. Lembre-se de respeitar os termos de serviço e políticas de uso do site que você está raspando.
