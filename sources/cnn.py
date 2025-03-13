from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CnnReader:

    urls = {
        'economy': 'https://www.cnnbrasil.com.br/economia/',
        'sports': 'https://www.cnnbrasil.com.br/esportes/',
        'entertainment': 'https://www.cnnbrasil.com.br/pop/',
        'politics': 'https://www.cnnbrasil.com.br/politica/',
    }
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def attatch_news(self, report):
        for topic in self.urls:
            self.driver.get(self.urls[topic])

            first_news = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".three__highlights__titles.three__highlights__titles--main.has--thumb a"))            )

            first_news.click()
            news_detail = self.__extract_first_news()
            report[topic].append(news_detail)

    def __extract_first_news(self):
        try:
            title = self.driver.find_element(By.CLASS_NAME, 'single-header__title').text
            description = self.driver.find_element(By.CLASS_NAME, 'single-header__excerpt').text
            imageUrl = self.driver.find_element(By.CLASS_NAME, 'featured-image__img').get_attribute('src')
            url = self.driver.find_element(By.CSS_SELECTOR, "meta[name='parsely-link']").get_attribute("content")

            return {
                'title': title,
                'description': description,
                'imageUrl': imageUrl,
                'url': url
            }
        except Exception as e:
            print(f'Error while extracting CNN news: {type(e).__name__}')
