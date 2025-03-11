# # Importações
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from time import sleep

# class UOLReader:
#     def __init__(self):
#         # Configuração do WebDriver para o UOL
#         options = webdriver.ChromeOptions()
#         options.add_argument("--disable-javascript")
#         self.driver = webdriver.Chrome(options=options)

#     def get_entertainment_news(self):
#         """Coleta a notícia principal de entretenimento no UOL."""
#         news_list = []

#         try:
#             # Acessa a página de política do UOL
#             self.driver.get("https://www.uol.com.br/splash/")

#             # Captura o primeiro link de notícia principal
#             noticia_principal = self.driver.find_element(
#                 By.XPATH, '/html/body/div[4]/div/div/div/a'
#             ).get_attribute('href')

#             print(noticia_principal)
#             # Percorre o único link coletado
#             self.driver.get(noticia_principal)
#             sleep(4)

#             # Captura a URL atual
#             url_atual = self.driver.current_url
#             print(f"URL da notícia acessada: {url_atual}")

#             # Coleta as informações principais da notícia
#             dados_geral = self.driver.find_element(By.XPATH, '/html/body/div[1]/main')

#             noticia = {
#                 "titulo": dados_geral.find_element(By.TAG_NAME, 'h1').text,
#                 "data": dados_geral.find_element(By.TAG_NAME, 'time').text,
#                 "resumo": dados_geral.find_element(By.TAG_NAME, 'p').text,
#                 "url": url_atual,
#             }

#             news_list.append(noticia)

#         except Exception as e:
#             print(f"Erro ao coletar notícias de entretenimeto: {e}")

#         return news_list

#     def attatch_news(self, report):
#         report["entertainment"].extend(self.get_entertainment_news())

#     def quit(self):
#         self.driver.quit()