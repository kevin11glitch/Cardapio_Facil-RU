# 🍽️ Cardápio Fácil RU - Automação e Notificação

Um bot estruturado em Python para extração automatizada de dados, projetado para realizar o web scraping diário do cardápio do Restaurante Universitário da Universidade Federal do Ceará (UFC), Campus Russas. A aplicação opera de forma 100% autônoma através de pipelines de Integração Contínua (CI), postando os dados processados diretamente em um canal do Telegram.

## 🚀 Funcionalidades e Arquitetura

O projeto foi desenhado com foco em resiliência, automação de rotinas e zero intervenção manual:

*   **Extração de Dados:** Web scraping diário do site institucional da universidade para coletar as opções do cardápio de forma automatizada.
*   **Integração Contínua (CI/CD):** Pipeline configurada no GitHub Actions com agendamento via *Cron Jobs*, garantindo a execução autônoma do script no horário estipulado.
*   **Notificação via API:** Integração direta com a API do Telegram para formatação e envio imediato das informações processadas aos canais de comunicação.
*   **Gestão de Segredos e Segurança:** Utilização de repositórios de *Secrets* do GitHub Actions para armazenar chaves de API e tokens, garantindo que credenciais sensíveis não fiquem expostas no código-fonte.

## 🛠️ Tecnologias Utilizadas

*   **Python 3:** Linguagem base para a estruturação lógica do bot.
*   **GitHub Actions:** Orquestração de CI/CD para execução contínua e agendamento de tarefas (DevOps).
*   **Telegram Bot API:** Plataforma de mensageria utilizada para o recebimento dos alertas.
*   **Bibliotecas Python:** `requests`, `BeautifulSoup`

## ⚙️ Como Executar Localmente

Para fins de teste, desenvolvimento e execução fora da pipeline estruturada, você pode rodar o bot no seu ambiente local:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/kevin11glitch/Cardapio_Facil-RU.git
   cd Cardapio_Facil-RU
  
2. **Instale as dependências:**
Certifique-se de ter o Python instalado e rode o comando abaixo para instalar as bibliotecas necessárias:

  ```bash
     pip install -r requirements.txt
  ```

3. **Configure as Variáveis de Ambiente:**
O script necessita de credenciais para se comunicar com o Telegram. Exporte as variáveis no seu terminal ou configure seu ambiente local com os dados do seu bot:

  ```bash
  TELEGRAM_TOKEN=seu_token_de_acesso_aqui
  CHAT_ID=id_do_canal_ou_grupo_de_destino
  ```

4. **Execute o script:**
  ```bash
  python main.py
  ```

## 🔄 Fluxo de Automação (GitHub Actions)
A principal entrega técnica deste repositório é a sua independência de infraestrutura local. O repositório possui um workflow configurado para rodar a aplicação em contêineres efêmeros do GitHub. A rotina inclui:

* Provisionamento do ambiente de execução (ex: ubuntu-latest).
* Instalação e configuração da versão correta do Python.
* Instalação das dependências via requirements.txt.
* Execução do script injetando os secrets (Tokens) no ambiente para comunicação autenticada e segura com a API do Telegram.

## 🎓 Contexto Acadêmico
Desenvolvido por Kevin Iohan Mendes de Sousa, estudante de Engenharia de Software na Universidade Federal do Ceará (UFC). Este projeto demonstra a aplicação prática de automação de rotinas, DevOps (CI/CD) e integração de APIs para a resolução de problemas reais de logística e comunicação no ecossistema universitário.
