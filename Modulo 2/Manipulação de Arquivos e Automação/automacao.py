# instalar o pyautogui com: pip install pyautogui
# crie uma automação que abra ayutomaticamente no navegador 

# Importamos a biblioteca para o script em uso
import pyautogui

# press é um comando que utilizamos para 
# Pressionar a tecla desejada 
pyautogui.press('Win') #para pressionar a tecla windows

# sleep é um comando para deixar o código em espera
# por alguns momentos
pyautogui.sleep(1)

# write é um comando para passar o que queremos 
# escrever
pyautogui.write('Google chrome')

pyautogui.press('Enter')
