import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 1

link = "LINK DO SEU SITE AQUI"

tabela = pd.read_csv("ARQUIVO CSV AQUI")

pyautogui.press("win")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(4)

pyautogui.click(x=822, y=396)
pyautogui.write("seuemail@gmail.com")
pyautogui.press("tab")
pyautogui.write("suasenha123")
pyautogui.click(x=982, y=557)

time.sleep(3)

for linha in tabela.index:
    pyautogui.click(x=831, y=279)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.click(x=913, y=933)

