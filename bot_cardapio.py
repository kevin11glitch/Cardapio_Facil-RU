import requests
from bs4 import BeautifulSoup
import os

TOKEN = os.getenv("TELEGRAM_TOKEN", "8638078098:AAFopqfkS-2_qW7qpfOH1forik73U1W-TdA")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "-5067991756")

def enviar_telegram(texto_cardapio):
    url_api = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": texto_cardapio,
        "parse_mode": "Markdown"
    }

    try:
        res = requests.post(url_api, data=payload)
        if res.status_code == 200:
            print("Cardápio enviado com sucesso para o Telegram!")
        else:
            print(f"Erro no Telegram: {res.text}")
    except Exception as e:
        print(f"Falha ao conectar com o Telegram: {e}")

def pegar_cardapio():
    url = "https://www.ufc.br/restaurante/cardapio/3-restaurante-universitario-de-russas"
    headers = {'User-Agent': 'Mozilla/5.0'}
    mensagem = ""

    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8' 
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            dia_tag = soup.find(class_='atual')
            if dia_tag:
                texto_dia = dia_tag.get_text(strip=True)
                print(f"DEBUG: Dia atual detectado: {texto_dia}")
            else:
                return "Cardápio não encontrado (Erro na tag de data)."

            tabelas = soup.find_all('table', class_=['almoco', 'jantar'])

            for tabela in tabelas:
                classes = tabela.get('class', [])
                tipo = "ALMOÇO" if "almoco" in classes else "JANTAR" if "jantar" in classes else "REFEIÇÃO"

                mensagem += f"\n*=== {tipo} - {texto_dia} ===*\n"

                for linha in tabela.find_all('tr'):
                    colunas = linha.find_all('td')
                    if len(colunas) >= 2:
                        categoria = colunas[0].get_text(strip=True)
                        celula_pratos = colunas[1]
                        
                        spans = celula_pratos.find_all('span')
                        if spans:
                            itens = [s.get_text(strip=True) for s in spans if s.get_text(strip=True)]
                            prato_formatado = ", ".join(itens)
                        else:
                            prato_formatado = celula_pratos.get_text(strip=True)
                        
                        if categoria and prato_formatado:
                            mensagem += f"• *{categoria}:* {prato_formatado}\n"
            
            return mensagem if mensagem else "Cardápio vazio ou não publicado."
    except Exception as e:
        return f"Erro na raspagem: {e}"

if __name__ == "__main__":
    print("Iniciando bot de cardápio...")
    resultado = pegar_cardapio()
    
    if "===" in resultado:
        print("Cardápio extraído. Enviando para o Telegram...")
        enviar_telegram(resultado)
    else:
        print(f"Aviso: {resultado}")