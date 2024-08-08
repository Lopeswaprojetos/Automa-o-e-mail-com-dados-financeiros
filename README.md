# Email Automation with Finance Data

Este projeto contém um script Python que automatiza o envio de e-mails com análises financeiras usando `pyautogui`, `pyperclip`, `yfinance`, e `webbrowser`. O script coleta dados históricos de ações e envia um e-mail contendo essas análises.

## Funcionalidades

- Solicita o código da ação desejada.
- Obtém dados financeiros da ação usando o `yfinance`.
- Calcula a cotação máxima, mínima e valor médio da ação.
- Automatiza o envio de um e-mail com as análises usando o `pyautogui` e `webbrowser`.

## Tecnologias Utilizadas

- **`pyautogui`**: Automatiza a interface gráfica do usuário para enviar e-mails.
- **`pyperclip`**: Facilita a manipulação da área de transferência para copiar e colar textos.
- **`yfinance`**: Coleta dados financeiros históricos das ações.
- **`webbrowser`**: Abre o navegador para acessar o Gmail.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `pyautogui`
  - `pyperclip`
  - `yfinance`
  - `webbrowser` (incluída no Python padrão)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Lopeswaprojetos/Automa-o-e-mail-com-dados-financeiros.git

2. **Navegue para o diretório do projeto**:
cd EmailAutomationWithFinance

3. **Instale as dependências**:
pip install pyautogui pyperclip yfinance

## Uso

1. **Execute o script**:
python projetofinanca.py

2. **Siga as instruções no terminal**: 
Siga as instruções no terminal para inserir o código da ação.

3. **Aguarde o script**:  
abrir o Gmail e enviar o e-mail automaticamente.

## Observações

Certifique-se de ajustar as coordenadas no código conforme necessário para o seu ambiente de trabalho.
O Gmail deve estar acessível e o navegador deve estar configurado para permitir que o pyautogui interaja com a interface.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou encontrar problemas, sinta-se à vontade para abrir um issue ou enviar um pull request.

