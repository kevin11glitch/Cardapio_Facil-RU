import requests
from bs4 import BeautifulSoup
from datetime import datetime
import locale

dia_numero = datetime.now().weekday()

dias_semana = {
    0: "Segunda-feira",
    1: "Terça-feira",
    2: "Quarta-feira",
    3: "Quinta-feira",
    4: "Sexta-feira",
    5: "Sábado",
    6: "Domingo"
}

dia_hoje = dias_semana.get(dia_numero)

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
                print(f"DEBUG: Dia atual detectado no site: {texto_dia}")
            else:
                return "Cardápio não encontrado (Erro na tag de data)."

            tabelas = soup.find_all('table', class_=['almoco', 'jantar'])

            for tabela in tabelas:
                classes = tabela.get('class', [])
                tipo = "ALMOÇO" if "almoco" in classes else "JANTAR" if "jantar" in classes else "REFEIÇÃO"

                mensagem += f"\n*=== {tipo} - {texto_dia} ===*\n"

                linhas = tabela.find_all('tr')
                for linha in linhas:
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
        return f"Erro: {e}"

if __name__ == "__main__":
    resultado = pegar_cardapio()
    print(resultado)