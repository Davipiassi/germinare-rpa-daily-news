import pyautogui
import keyboard  # Biblioteca para detectar a tecla pressionada

print("Mova o mouse para a posição desejada e pressione 'Enter' para capturar as coordenadas.")
print("Pressione 'Esc' para sair.")

while True:
    if keyboard.is_pressed("enter"):  # Quando a tecla 'Enter' for pressionada
        x, y = pyautogui.position()  # Obtém as coordenadas atuais
        print(f"Coordenadas capturadas: X={x}, Y={y}")
        
        while keyboard.is_pressed("enter"):  # Aguarda a tecla ser solta
            pass  # Evita múltiplas capturas seguidas

    if keyboard.is_pressed("esc"):  # Pressione 'Esc' para sair
        print("Saindo...")
        break
    