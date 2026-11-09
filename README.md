# AutoCadastro-Py (Bot de Automação de Cadastros)

Este projeto é uma automação desenvolvida em Python (RPA - Robotic Process Automation) projetada para ler dados de um arquivo CSV e cadastrá-los automaticamente em um sistema web. O bot simula as ações humanas de abrir o navegador, fazer login, clicar em campos de texto e digitar as informações.

## 🚀 Como funciona

O projeto possui dois arquivos principais:

1.  **`localizador_mouse.py`**: Um script auxiliar para capturar as coordenadas (X, Y) do seu mouse. Isso é necessário porque a resolução e o tamanho do monitor variam de usuário para usuário.
2.  **`main.py`**: O script principal que executa a automação. Ele utiliza o `pandas` para ler os dados da planilha e o `pyautogui` para controlar o mouse e o teclado.

## 📋 Pré-requisitos

Para rodar este projeto, você precisará ter o [Python](https://www.python.org/downloads/) instalado na sua máquina. Além disso, é necessário instalar as bibliotecas de terceiros utilizadas no código.

Abra o seu terminal (Prompt de Comando ou PowerShell) e digite o seguinte comando:

```bash
pip install pyautogui pandas openpyxl
```
*(Nota: o `openpyxl` é instalado frequentemente junto com o pandas para evitar erros de leitura de planilhas caso queira expandir para Excel).*

## ⚙️ Configuração e Adaptação

Como a biblioteca `pyautogui` funciona à base de **coordenadas da tela**, o código não funcionará perfeitamente em outro computador se não houver um ajuste prévio, pois a posição dos botões no seu monitor será diferente da posição no monitor de outra pessoa.

### 1. Mapeando a sua tela
Para descobrir as coordenadas exatas dos botões no seu monitor:
1. Abra o site do sistema que você quer automatizar no seu navegador.
2. Execute o arquivo `localizador_mouse.py`.
3. Você tem **5 segundos** para colocar o cursor do mouse em cima do campo ou botão que deseja clicar.
4. O terminal imprimirá a posição (Exemplo: `Point(x=822, y=396)`).
5. Anote esses valores.

### 2. Ajustando o `main.py`
Substitua os seguintes pontos no script principal antes de rodar:
*   **Link do site**: Altere `"LINK DO SEU SITE AQUI"` para a URL real do sistema.
*   **Base de dados**: Altere `"ARQUIVO CSV AQUI"` para o nome do arquivo que será disponibilizado neste repositório (ex: `"produtos.csv"`).
*   **Navegador**: O código está configurado para abrir o `"Navegador Opera GX"`. Se você usa o Google Chrome, altere o texto no `pyautogui.write()` na linha 11.
*   **Coordenadas de Login e Botões**: Substitua os valores de `x` e `y` nos comandos `pyautogui.click()` com os valores que você mapeou no passo anterior.

## ▶️ Como Executar

Após configurar as coordenadas e os nomes dos arquivos, basta rodar o script principal no terminal:

```bash
python main.py
```

**⚠️ Aviso Importante (Failsafe):**
Para interromper a automação a qualquer momento (caso o mouse comece a clicar no lugar errado), basta **arrastar o cursor do mouse rapidamente para qualquer um dos quatro cantos extremos da sua tela**. Isso aciona o sistema de segurança do PyAutoGUI (FailSafeException) e encerra o programa imediatamente.

## 📁 Estrutura do CSV

O arquivo CSV esperado para esta automação deve conter as seguintes colunas (na primeira linha / cabeçalho):
*   `codigo`
*   `marca`
*   `tipo`
*   `categoria`
*   `preco_unitario`
*   `custo`
*   `obs`