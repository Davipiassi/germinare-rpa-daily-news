import pyautogui
import time
import os
import pygetwindow as gw

class SendEmail:
    
    def sendNewsLetter(self, pdf_path):
        nome_arquivo = os.path.basename(pdf_path)

        os.startfile("outlook")  
        time.sleep(5)

        pyautogui.hotkey("ctrl", "o")
        time.sleep(2)

        pyautogui.click(1471, 86)

        pyautogui.write("raphael.silva@germinare.org.br")
        pyautogui.press("tab") 
        pyautogui.press("tab")

        pyautogui.write("Assunto: Enviando NewsLetter")
        pyautogui.press("tab")

        pyautogui.write("Parabéns! Você acaba de receber uma newsletter cheia de notícias legais (ou não)")
        time.sleep(1)

        #clica no botão de anexar arquivo
        pyautogui.click(1024, 163)
        time.sleep(4)
        pyautogui.click(1192, 951)
        time.sleep(4)

        windows = gw.getAllTitles()

        # Verifica se alguma janela do Explorador está aberta
        if any("Explorador de Arquivos" in w or "File Explorer" in w for w in windows):
            print("Explorador de Arquivos aberto!")
        else:
            pyautogui.click(941, 137)
            pyautogui.click(1192, 951)
            time.sleep(4)
            print("Explorador de Arquivos não abriu.")

        #scrollar
        pyautogui.moveTo(140, 355)
        pyautogui.scroll(500)
        time.sleep(2)

        pyautogui.click(85, 190)
        time.sleep(2)

        pyautogui.click(743, 83)
        time.sleep(2)

        pyautogui.write(nome_arquivo)
        pyautogui.press("enter")
        time.sleep(5)

        pyautogui.click(564, 200)
        time.sleep(2)

        pyautogui.hotkey("ctrl", "enter")
        time.sleep(2)

        print("E-mail enviado com sucesso!")
