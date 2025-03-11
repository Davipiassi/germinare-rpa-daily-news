from threading import Thread
from selenium import webdriver
from sources.cnn import CnnReader
from sources.g1 import G1Reader
from sources.uol import UOLReader
import time

# Estrutura inicial do relatório
report = {
    'economy': [],
    'sports': [],
    'entertainment': [],
    'politics': [],
    'trending-topics': [],
    'coins': [],
}

def run_cnn_reader(report):
    driver = webdriver.Chrome()  
    cnn_reader = CnnReader(driver)
    try:
        cnn_reader.noticias_cnn(report)
    finally:
        cnn_reader.driver.quit()

def run_g1_reader(report):
    driver = webdriver.Chrome()  
    g1_reader = G1Reader(driver)
    try:
        g1_reader.attatch_news(report)
    finally:
        g1_reader.driver.quit()

def run_uol_reader(report):
    uol_reader = UOLReader()
    try:
        uol_reader.attach_news(report)
    finally:
        uol_reader.quit()

def main():
    # Cria as threads para os leitores
    cnn_thread = Thread(target=run_cnn_reader, args=(report,))
    g1_thread = Thread(target=run_g1_reader, args=(report,))
    uol_thread = Thread(target=run_uol_reader, args=(report,))

    # Inicia as threads
    cnn_thread.start()
    g1_thread.start()
    uol_thread.start()

    # Aguarda todas as threads finalizarem
    cnn_thread.join()
    g1_thread.join()
    uol_thread.join()

# Executa a função main
main()

# Exibe o relatório final
print(report)