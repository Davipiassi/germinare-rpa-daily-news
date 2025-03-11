from threading import Thread
from selenium import webdriver
from sources.g1 import G1Reader
from sources.uol import UOLReader

# Estrutura inicial do relatório
report = {
    'economy': [],
    'sports': [],
    'entertainment': [],
    'politics': [],
    'trending-topics': [],
    'coins': [],
}

def run_g1_reader(report):
    g1_reader = G1Reader(webdriver.Chrome())
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
    # Cria threads para os leitores
    g1_thread = Thread(target=run_g1_reader, args=(report,))
    uol_thread = Thread(target=run_uol_reader, args=(report,))

    # Inicia as threads
    g1_thread.start()
    uol_thread.start()

    # Aguarda ambas as threads finalizarem
    g1_thread.join()
    uol_thread.join()

main()

# Exibe o relatório final
print(report)
