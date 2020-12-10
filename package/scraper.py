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

def consigliati_scraper():
    global book_dict
    navigate_to_soup('https://www.ibs.it/libri-consigliati-da-leggere')
    main = soup.find("div", {"class": "modulo-ctn mdl-listaprodotti padding-sp padding-top"})
    sections = main.findAll("div",{"class":"box-body"})
    book_dict = {}
    index = 1
    print("\n")
    print(color.BOLD +"Ecco qui i libri consigliati della settimana:"+ color.END)
    for section in sections:
        book_name = section.find("h5",{"class":"subtitle"}).text.strip()
        author_container = section.find("div",{"class":"box-title-prd"})
        author = author_container.h3.text.strip()
        plot_container = section.find("div",{"class":"abstract"})
        plot = plot_container.p.text.strip()
        link = ("https://www.ibs.it"+section.figure.a['href'])
        book_info = [author, book_name, plot, link]
        book_dict[index] = book_info
        print(str(index)+". "+book_name+"  ("+author+")")
        index += 1
    print("\n")
    builtins.book_dict = book_dict