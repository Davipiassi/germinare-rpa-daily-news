from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class UOLReader:
    
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-javascript")
        self.driver = webdriver.Chrome(options=options)

    def get_news(self, url, news_xpath):
        news_list = []

        try:
            self.driver.get(url)

            first_news = self.driver.find_element(By.XPATH, news_xpath).get_attribute('href')
            self.driver.get(first_news)
            sleep(4)

            current_url = self.driver.current_url

            news_data = self.driver.find_element(By.XPATH, '/html/body/div[1]/main')

            news = {
                "title": news_data.find_element(By.TAG_NAME, 'h1').text,
                "date": news_data.find_element(By.TAG_NAME, 'time').text,
                "description": news_data.find_element(By.TAG_NAME, 'p').text,
                "url": current_url,
            }

            news_list.append(news)

        except Exception as e:
            print(f'Error while extracting UOL news: {type(e).__name__}')
            
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