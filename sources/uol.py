from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class UOLReader:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-javascript")
        self.driver = webdriver.Chrome(options=options)

    def get_news(self, url, news_xpath):
        """Coleta a notícia principal de uma seção específica do UOL."""
        news_list = []

        try:
            # Acessa a página da seção
            self.driver.get(url)

            # Captura o primeiro link de notícia principal
            noticia_principal = self.driver.find_element(By.XPATH, news_xpath).get_attribute('href')

            # Acessa o link da notícia
            self.driver.get(noticia_principal)
            sleep(4)

            # Captura a URL atual
            url_atual = self.driver.current_url
            print(f"URL da notícia acessada: {url_atual}")

            # Coleta as informações principais da notícia
            dados_geral = self.driver.find_element(By.XPATH, '/html/body/div[1]/main')

            noticia = {
                "titulo": dados_geral.find_element(By.TAG_NAME, 'h1').text,
                "data": dados_geral.find_element(By.TAG_NAME, 'time').text,
                "description": dados_geral.find_element(By.TAG_NAME, 'p').text,
                "url": url_atual,
            }

            news_list.append(noticia)

        except Exception as e:
            print(f"Erro ao coletar notícias: {e}")
            # Adiciona None para os campos no dicionário em caso de erro
            news_list.append({
                "titulo": None,
                "data": None,
                "description": None,
                "url": None,
            })

        return news_list
    
    def get_economy_news(self):
            return self.get_news(
                url="https://economia.uol.com.br/",
                news_xpath="/html/body/div[4]/section/div/div/div[1]/div/div/a"
            ) 
    
    def get_sports_news(self):
        return self.get_news(
            url="https://www.uol.com.br/esporte/",
            news_xpath="/html/body/div[5]/div/div/div/div/div/a"
        )
    
    def get_entertainment_news(self):
        return self.get_news(
            url="https://www.uol.com.br/splash/",
            news_xpath="/html/body/div[4]/section/div/div/div[1]/div/div/a"
        )
    
    def get_politics_news(self):
        return self.get_news(
            url="https://noticias.uol.com.br/politica/",
            news_xpath="/html/body/div[4]/section/section/div/div/div[1]/section/div/div/div/div/div[1]/div/a"
        )

    def attach_news(self, report):
        report["politics"].extend(self.get_politics_news())
        report["economy"].extend(self.get_economy_news())
        report["sports"].extend(self.get_sports_news())
        report["entertainment"].extend(self.get_entertainment_news())


    def quit(self):
        self.driver.quit()