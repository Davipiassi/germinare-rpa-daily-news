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
        self.driver.get(self.url)
        
        try:
            time.sleep(3)
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.view-all-btn")))
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            button.click()

            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".trend-card__list li"))            )
            
            trend_items = self.driver.find_elements(By.CSS_SELECTOR, ".trend-card__list li")
            trends = []
            
            for item in trend_items[:10]:
                try:
                    name_element = item.find_element(By.CSS_SELECTOR, ".trend-name a")
                    name = name_element.text if name_element.text else "N/A"
                    link = name_element.get_attribute("href")
                    
                    try:
                        count = item.find_element(By.CSS_SELECTOR, ".tweet-count").text
                    except:
                        count = "N/A"
                    
                    trends.append({"name": name, "tweets": count, "link": link})
                except Exception as e:
                    print(f"Error processing a trend item: {type(e).__name__}")
            
            report["trending"] = trends
        
        except Exception as e:
            print(f"Error accessing trends: {type(e).__name__}")