from selenium import webdriver
from sources.g1 import G1Reader

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
    
    g1_reader = G1Reader(driver)
    
    g1_reader.attatch_news(report)

main()

print(report)
    

