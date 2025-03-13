from threading import Thread
from selenium import webdriver
from sources.cnn import CnnReader
from sources.g1 import G1Reader
from sources.uol import UOLReader
from sources.trending import TrendingReader
from sources.report import NewsReport
from sources.sendEmail import SendEmail
from selenium.webdriver.chrome.options import Options
import time

report = {
    'economy': [],
    'sports': [],
    'entertainment': [],
    'politics': [],
    'trending': [],
}

def run_cnn_reader(report):
    option = Options()
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
    driver = webdriver.Chrome(options=option)  
    cnn_reader = CnnReader(driver)  
    try:
        cnn_reader.attatch_news(report)
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
        
def run_trending_reader(report):
    driver = webdriver.Chrome()  
    trending_reader = TrendingReader(driver)
    try:
        trending_reader.attatch_trending(report)
    finally:
        trending_reader.driver.quit()

def main():
    cnn_thread = Thread(target=run_cnn_reader, args=(report,))
    g1_thread = Thread(target=run_g1_reader, args=(report,))
    uol_thread = Thread(target=run_uol_reader, args=(report,))
    trending_thread = Thread(target=run_trending_reader, args=(report,))

    cnn_thread.start()
    g1_thread.start()
    uol_thread.start()
    trending_thread.start()

    cnn_thread.join()
    g1_thread.join()
    uol_thread.join()
    trending_thread.join()
    
    report_generator = NewsReport(report)
    pdf_path = report_generator.generate_pdf()
    print(pdf_path)
    
    email_sender = SendEmail()
    email_sender.sendNewsLetter(pdf_path)


main()
# print(report)