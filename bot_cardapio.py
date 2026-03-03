import requests
from bs4 import BeautifulSoup

def pegar_cardapio():
    url = "https://www.ufc.br/restaurante/cardapio/3-restaurante-universitario-de-russas"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8' 
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            titulo = soup.find('h2').text if soup.find('h2') else "Site acessado!"
            print(f"Sucesso: {titulo}")
        else:
            print(f"Erro ao acessar o site: {response.status_code}")
            
    except Exception as e:
        print(f"Erro na conexão: {e}")

if __name__ == "__main__":
    pegar_cardapio()