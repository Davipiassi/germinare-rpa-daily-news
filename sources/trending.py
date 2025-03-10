import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TrendingReader:
    
    url = "https://trends24.in/brazil/"
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        
    def attatch_trending(self, report):
        print(f'Accessing Trending {self.url}')
        self.driver.get(self.url)
        
        try:
            time.sleep(3)
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.view-all-btn"))
            )
            
            # Rolando até o botão para garantir que o botão está visível e não bloqueado
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            button.click()
            print("Clicked 'View all 50 trends' button")

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".trend-card__list li"))
            )
            
            trend_items = self.driver.find_elements(By.CSS_SELECTOR, ".trend-card__list li")
            trends = []
            
            for item in trend_items[:10]:
                try:
                    nome_element = item.find_element(By.CSS_SELECTOR, ".trend-name a")
                    nome = nome_element.text if nome_element.text else "N/A"
                    link = nome_element.get_attribute("href")
                    
                    try:
                        count = item.find_element(By.CSS_SELECTOR, ".tweet-count").text
                    except:
                        count = "N/A"
                    
                    trends.append({"nome": nome, "tweets": count, "link": link})
                except Exception as e:
                    print(f"Error processing a trend item: {e}")
            
            report["trending"] = trends
            print("Trending topics collected successfully!")
        
        except Exception as e:
            print(f"Error accessing trends: {e}")

from selenium import webdriver

driver = webdriver.Chrome()
report = {}
reader = TrendingReader(driver)
reader.attatch_trending(report)
print(report)
driver.quit()
