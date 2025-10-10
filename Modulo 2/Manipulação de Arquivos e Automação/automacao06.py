import pyautogui
import webbrowser
import time 

# Passo 1: abri o youtube com uma música específica
url = 'https://www.youtube.com/watch?v=X791IzOwt3Q&list=RDX791IzOwt3Q&start_radio=1'
webbrowser.open(url)

# aguardar o carregamneto da página
time.sleep(5) # ajustar de acordo com a velocidade da net

# Aperte espaço para dar o play no vídeo
pyautogui.press('space') # toca ou pausa o vídeo