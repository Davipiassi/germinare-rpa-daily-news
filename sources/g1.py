from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class G1Reader:
    
    urls = {
        'economy': 'https://g1.globo.com/economia/',
        'sports': 'https://ge.globo.com/',
        'entertainment': 'https://gshow.globo.com/',
        'politics': 'https://g1.globo.com/politica/',
    }
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        
    def attatch_news(self, report):
        for topic in self.urls:
            self.driver.get(self.urls[topic])
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'feed-post-body')))
            
            topic_news_list = self.driver.find_elements(By.CLASS_NAME, 'feed-post-body')
            
            if topic == 'entertainment':
                news = self.__extract_entertainment_first_news(topic_news_list)
                report[topic].append(news)
            else:
                news = self.__extract_first_news(topic_news_list)
                report[topic].append(news)
            
    def __extract_first_news(self, news_list):       
        for news in news_list:
            try:
                title = news.find_element(By.CLASS_NAME, 'feed-post-body-title').find_element(By.TAG_NAME, 'p').text
                description = news.find_element(By.CLASS_NAME, 'feed-post-body-resumo').find_element(By.TAG_NAME, 'p').text
                imageUrl = news.find_element(By.CLASS_NAME, 'bstn-fd-picture-image').get_attribute('src')
                url = news.find_element(By.CLASS_NAME, 'feed-post-body-title').find_element(By.TAG_NAME, 'a').get_attribute('href')
                
                return {
                    'title': title,
                    'description': description,
                    'imageUrl': imageUrl,
                    'url': url
                }
            except Exception as e:
                print(f'Error while extracting these news: {type(e).__name__}')
                continue
            
    def __extract_entertainment_first_news(self, news_list):
        for news in news_list:
            try:
                title = news.find_element(By.CLASS_NAME, 'post-materia-text__title').text
                description = news.find_element(By.CLASS_NAME, 'post-materia-text__description').text
                imageUrl = news.find_element(By.CLASS_NAME, 'bstn-fd-cover-picture').find_element(By.TAG_NAME, 'img').get_attribute('src')
                url = news.find_element(By.CLASS_NAME, 'post-materia-text').get_attribute('href')
                
                return {
                    'title': title,
                    'description': description,
                    'imageUrl': imageUrl,
                    'url': url
                }
            except Exception as e:
                print(f'Error while extracting these news: {type(e).__name__}')
                continue