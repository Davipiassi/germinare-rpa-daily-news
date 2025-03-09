from selenium import webdriver
from cnn import CnnReader

report = {
    'economy': [],
    'sports': [],
    'entertainment': [],
    'politics': [],
    'trending-topics': [],
    'coins': [],
}

def main():
    driver = webdriver.Chrome()
    
    cnnReader = CnnReader(driver)
    
    cnnReader.noticias_cnn

main()

print(report)
    