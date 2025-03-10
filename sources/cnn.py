from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CnnReader:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    urls = {
        'economy': 'https://www.cnnbrasil.com.br/economia/',
        'sports': 'https://www.cnnbrasil.com.br/esportes/',
        'entertainment': 'https://www.cnnbrasil.com.br/pop/',
        'politics': 'https://www.cnnbrasil.com.br/politica/',
    }

    def noticias_cnn(self, report):

        for topic in self.urls:
            self.driver.get(self.urls[topic])

            wait = WebDriverWait(self.driver, 10)

            primeira_noticia = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".three__highlights__titles.three__highlights__titles--main.has--thumb a"))
            )

            primeira_noticia.click()
            print("Primeira notícia aberta com sucesso!")
            detalhes_noticia = self.extrair_noticia()
            report[topic].append(detalhes_noticia)

    def extrair_noticia(self):
        try:
            title = self.driver.find_element(By.CLASS_NAME, 'single-header__title').text
            description = self.driver.find_element(By.CLASS_NAME, 'single-header__excerpt').text
            imageUrl = self.driver.find_element(By.CLASS_NAME, 'featured-image__img').get_attribute('src')
            url = self.driver.find_element(By.CSS_SELECTOR, "meta[name='parsely-link']").get_attribute("content")

            print('Notícia extraída com sucesso!')
            return {
                'title': title,
                'description': description,
                'imageUrl': imageUrl,
                'url': url
            }
        except Exception as e:
            print(f'Erro ao extrair notícia: {type(e).__name__}')