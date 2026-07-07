"""
Projeto: Automação de Cadastro de Produtos

Descrição:
Automação de cadastro de produtos em sistema web utilizando Python.

Tecnologias:
- Python
- Pandas
- PyAutoGUI

Objetivo:
Automatizar tarefas repetitivas, reduzindo processos manuais
e aumentando eficiência operacional.
"""


import time
import pyautogui
import pandas as pd


# Configuração da automação
pyautogui.PAUSE = 0.3


# ==========================================
# 1 - Abrir navegador
# ==========================================

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)


# ==========================================
# 2 - Acessar sistema
# ==========================================

pyautogui.write(
    "https://sistemadaempresaaqui.com/login"
)

pyautogui.press("enter")

time.sleep(3)


# ==========================================
# 3 - Login
# ==========================================

pyautogui.click(x=685, y=451)

pyautogui.write("SEU_EMAIL_AQUI")

pyautogui.press("tab")

pyautogui.write("SUA_SENHA_AQUI")

pyautogui.click(x=955, y=638)

time.sleep(3)


# ==========================================
# 4 - Importar dados
# ==========================================

produtos = pd.read_csv("produtos.csv")


print(produtos)


# ==========================================
# 5 - Cadastro automático
# ==========================================

for linha in produtos.index:


    pyautogui.click(x=653, y=294)


    pyautogui.write(
        str(produtos.loc[linha, "codigo"])
    )

    pyautogui.press("tab")


    pyautogui.write(
        str(produtos.loc[linha, "marca"])
    )

    pyautogui.press("tab")


    pyautogui.write(
        str(produtos.loc[linha, "tipo"])
    )

    pyautogui.press("tab")


    pyautogui.write(
        str(produtos.loc[linha, "categoria"])
    )

    pyautogui.press("tab")


    pyautogui.write(
        str(produtos.loc[linha, "preco_unitario"])
    )

    pyautogui.press("tab")


    pyautogui.write(
        str(produtos.loc[linha, "custo"])
    )

    pyautogui.press("tab")


    observacao = produtos.loc[linha, "obs"]


    if pd.notna(observacao):

        pyautogui.write(
            str(observacao)
        )


    pyautogui.press("tab")

    pyautogui.press("enter")


    pyautogui.scroll(5000)



print("Cadastro finalizado com sucesso!")