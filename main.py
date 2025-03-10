from selenium import webdriver
from selenium.webdriver.common.by import By

news = {
    'economy': [],
    'sports': [],
    'entertainment': [],
    'politics': [],
    'trending-topics': [],
    'coins': [],
}

driver = webdriver.Chrome()
driver.get("https://trends24.in/brazil/")

driver.find_element(By.CLASS_NAME, "trend-card__list")



