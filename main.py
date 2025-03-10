from selenium import webdriver
from cnn import CnnReader
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
    
    cnnReader = CnnReader(driver)
    
    cnnReader.noticias_cnn

    g1_reader = G1Reader(driver)
    
    g1_reader.attatch_news(report)

print(report)