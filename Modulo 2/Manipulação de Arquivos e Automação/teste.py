import pyautogui
import time

# Pausa entre as ações para evitar erros
pyautogui.PAUSE = 0.2

# Função para desenhar um quadrado
def desenhar_quadrado(tamanho):
    # Pressiona o botão esquerdo do mouse para começar a desenhar
    pyautogui.mouseDown()
    for _ in range(4):  # Quadrado tem 4 lados
        pyautogui.moveRel(tamanho, 0)  # Move para a direita
        pyautogui.moveRel(0, tamanho)  # Move para baixo
        pyautogui.moveRel(-tamanho, 0)  # Move para a esquerda
        pyautogui.moveRel(0, -tamanho)  # Move para cima
    # Solta o botão do mouse
    pyautogui.mouseUp()

# Configuração inicial
print("Posicione o cursor onde deseja começar a desenhar.")
time.sleep(5)  # Dá tempo para o usuário posicionar o mouse

# Tamanho do quadrado (em pixels)
tamanho_quadrado = 100

# Chama a função para desenhar o quadrado
desenhar_quadrado(tamanho_quadrado)

print("Desenho concluído!")
