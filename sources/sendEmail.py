import pyautogui
import time
import os
import pygetwindow as gw

class SendEmail:
    
    def sendNewsLetter(self, pdf_path):
        caminho_arquivo = os.path.dirname(pdf_path)

        pyautogui.hotkey("win", "r")
        time.sleep(2)

        pyautogui.write(caminho_arquivo)
        pyautogui.press("enter")
        time.sleep(2)

        pyautogui.press("end")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(2)

        os.startfile("outlook")  
        time.sleep(8)

        window = gw.getWindowsWithTitle("Outlook")[0]
        time.sleep(10)
        window.maximize()

        pyautogui.hotkey("ctrl", "o")
        time.sleep(5)

        pyautogui.click(1471, 86)

        pyautogui.write("raphael.silva@germinare.org.br")
        pyautogui.press("tab") 
        pyautogui.press("tab")

        pyautogui.write("Assunto: Enviando NewsLetter")
        pyautogui.press("tab")

        pyautogui.write("Bom dia, gente bonita (e arrumadinhos)!!!")
        time.sleep(2)

        pyautogui.hotkey("ctrl", "v")
        time.sleep(3)

        pyautogui.click(81, 327)

        print("E-mail enviado com sucesso!")
