from bs4 import BeautifulSoup
import builtins
import time 

def navigate_to_soup(link):
    browser = builtins.browser
    browser.get(link)
    time.sleep(2)
    content = browser.page_source.encode('utf-8').strip()
    global soup
    soup = BeautifulSoup(content,"html.parser")