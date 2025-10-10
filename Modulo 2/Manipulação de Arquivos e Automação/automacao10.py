import pyautogui
import time 

pyautogui.press("Win")
time.sleep
pyautogui.write("Desenhando com pyautogui")
pyautogui.press("enter")
time.sleep(2)

arvore = [
    ""      '^'    ""
    ""      '^^^'    ""
    ""      '^^^^^'    ""
    ""      '||| '     ""
]

for linha in arvore:
    pyautogui.write(linha, interval=0.1)
    pyautogui.press("enter")
print("Desenho da árvore concluído")

