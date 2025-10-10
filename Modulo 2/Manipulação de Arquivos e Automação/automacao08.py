import pyautogui, time # outra maneira de escrever a importação
time.sleep(3)
pyautogui.write("aaluno_python  senha123" \
"aaluno_python  senha123luno_python senha123" \
"luno_python", interval=0.1)
pyautogui.press("tab")
pyautogui.write("senha123", interval=0.1)
pyautogui.press("enter")