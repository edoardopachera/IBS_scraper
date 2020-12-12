from bs4 import BeautifulSoup
import wikipedia
import builtins
import time


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def navigate_to_soup(link):
    """Uses the selenium browser to navigate to a inputed link.
    Saves the html into a BeautifulSoup object.
    """
    browser = builtins.browser
    browser.get(link)
    time.sleep(2)
    content = browser.page_source.encode('utf-8').strip()
    global soup
    soup = BeautifulSoup(content, "html.parser")


def consigliati_scraper():
    global book_dict
    global scelta
    global price
    navigate_to_soup('https://www.ibs.it/libri-consigliati-da-leggere')
    main = soup.find(
        "div",
        {"class": "modulo-ctn mdl-listaprodotti padding-sp padding-top"})
    sections = main.findAll("div", {"class": "box-body"})
    book_dict = {}
    index = 1
    print("\n")
    print(color.BOLD + "Ecco qui i libri consigliati della settimana:"
          + color.END)
    for section in sections:
        book_name = section.find("h5", {"class": "subtitle"}).text.strip()
        author_container = section.find("div", {"class": "box-title-prd"})
        author = author_container.h3.text.strip()
        plot_container = section.find("div", {"class": "abstract"})
        plot = plot_container.p.text.strip()
        link = ("https://www.ibs.it"+section.figure.a['href'])
        book_info = [author, book_name, plot, link]
        book_dict[index] = book_info
        print(str(index)+". "+book_name+"  ("+author+")")
        index += 1
    print("\n")
    builtins.book_dict = book_dict
    while True:
        print(color.BOLD
              + "Di quale libro vuoi avere più informazioni? (Inserire numero)"
              + color.END)
        scelta = input()
        try:
            scelta = int(scelta)
            if isinstance(scelta, int) is True and scelta in range(1, index):
                builtins.scelta = scelta
                break
            else:
                print("\n")
                print(color.BOLD + color.RED +
                      "Hai inserito un valore errato, prova di nuovo!"
                      + color.END)
        except ValueError:
            print("\n")
            print(color.BOLD + color.RED +
                  "Hai inserito un valore errato, prova di nuovo!"+color.END)
    libro_scelto = book_dict.get(scelta, None)
    autore_libro_scelto = libro_scelto[0]
    nome_libro_scelto = libro_scelto[1]
    link_libro_scelto = libro_scelto[3]
    plot_libro_scelto = libro_scelto[2]
    print("\n")
    print("Hai scelto: " + (color.PURPLE + color.BOLD + '"'
          + color.END) + (color.PURPLE + color.BOLD + "%s"
          + color.END) % (nome_libro_scelto)+(color.PURPLE
          + color.BOLD + '"' + color.END))
    navigate_to_soup(link_libro_scelto)

    price = soup.find(
        "h2", {"data-aid": "pdp_price_current-price"}).text.strip()
    builtins.price = price

    wikipedia.set_lang("it")
    try:
        about_the_author = wikipedia.summary(autore_libro_scelto, sentences=1)
    except:
        about_the_author = "Non sono presenti info su questo autore :("
    print("\n")
    print(color.BOLD + "Ecco maggiori info:" + color.END)
    print("\n")
    print((color.DARKCYAN+color.BOLD + "AUTORE:  " +
           color.END)+autore_libro_scelto.upper())
    print(about_the_author)
    print("\n")
    print((color.DARKCYAN+color.BOLD + "PREZZO:  "+color.END)+price)
    print("\n")
    print((color.DARKCYAN+color.BOLD + "TRAMA:  "+color.END)+plot_libro_scelto)
    time.sleep(3)
    print("\n")


def classifica_scraper():
    global book_dict
    global scelta

    navigate_to_soup(
        'https://www.ibs.it/classifica/libri/1week/sold?defaultPage=1')
    main = soup.find(
        "div",
        {"class": "col-lg-25 col-md-25 col-sm-25 col-xs-25 gridContainer"})
    sections = main.findAll(
        "li", {"class": "col-lg-5 col-md-5 col-sm-25 col-xs-25"})
    try:
        if book_dict != {}:
            for i in book_dict:
                print(str(i)+". "+((book_dict[i])[1]) +
                      "  ("+((book_dict[i])[0])+")")
    except NameError:
        book_dict = {}
        index = 1
        print("\n")
        print(color.BOLD +
              "Ecco qui i libri in classifica questa settimana:" + color.END)
        for section in sections:
            book_link_container = section.find(
                "div", {"class": "rankProductTitle"}).text.strip()
            link = ("https://www.ibs.it"+section.a['href'])
            navigate_to_soup(link)
            book_name = soup.find("h1", {"class": "title__text"}).text.strip()
            try:
                author = soup.find(
                    "h2",
                    {"class": "subline__title author__title"}).text.strip()
            except:
                author = 'Nessun autore indicato'
            price = soup.find(
                "h2", {"data-aid": "pdp_price_current-price"}).text.strip()
            plot_container = soup.find(
                "div", {"class": "abstract__description ibs-show-more"})
            plot = ''
            paragraphs = plot_container.div.findAll("p")
            for p in paragraphs:
                text = p.text.strip()
                plot += text
            book_info = [author, book_name, plot, link, price]
            book_dict[index] = book_info
            print(str(index)+". "+book_name+"  ("+author+")")
            index += 1
        builtins.book_dict = book_dict

        print("\n")
        while True:
            print(
                color.BOLD +
                "Di quale libro vuoi avere più informazioni? (Inserire numero)"
                + color.END)
            scelta = input()
            try:
                scelta = int(scelta)
                if isinstance(scelta, int) is True and scelta in range(1, index):
                    builtins.scelta = scelta
                    break
                else:
                    print("\n")
                    print(color.BOLD + color.RED +
                          "Hai inserito un valore errato, prova di nuovo!"
                          + color.END)
            except ValueError:
                print("\n")
                print(color.BOLD + color.RED +
                      "Hai inserito un valore errato, prova di nuovo!"
                      + color.END)
        libro_scelto = book_dict.get(scelta, None)
        libro_scelto = book_dict.get(scelta, None)
        autore_libro_scelto = libro_scelto[0]
        nome_libro_scelto = libro_scelto[1]
        link_libro_scelto = libro_scelto[3]
        plot_libro_scelto = libro_scelto[2]
        price_libro_scelto = libro_scelto[4]
        builtins.price = price_libro_scelto
        print("\n")
        print("Hai scelto: " + (color.PURPLE +
              color.BOLD + '"' + color.END)+(color.PURPLE + color.BOLD +
              "%s" + color.END) % (nome_libro_scelto) + (color.PURPLE
              + color.BOLD + '"' + color.END))

        wikipedia.set_lang("it")
        try:
            about_the_author = wikipedia.summary(
                autore_libro_scelto, sentences=1)
        except:
            about_the_author = "Non sono presenti info su questo autore :("
        print("\n")
        print(color.BOLD + "Ecco maggiori info:" + color.END)
        print("\n")
        print((color.DARKCYAN+color.BOLD + "AUTORE:  " +
               color.END)+autore_libro_scelto.upper())
        print(about_the_author)
        print("\n")
        print((color.DARKCYAN + color.BOLD +
               "PREZZO:  " + color.END)+price_libro_scelto)
        print("\n")
        print((color.DARKCYAN+color.BOLD +
               "TRAMA:  " + color.END) + plot_libro_scelto)
        time.sleep(3)
        print("\n")


def recursive():
    global y
    y = 1
    while True:
        print(color.BOLD+"Vuoi avere info su altri libri? [si/no]"+color.END)
        scelta = str(input())
        if scelta in ["sì", "si", "Si", "SI"]:
            y = 1
            print("\n")
            break
        elif scelta in ["no", "No", "NO"]:
            print("\n")
            print(color.BOLD+"Va bene, Arrivederci!"+color.END)
            y = 2
            break
        else:
            print("\n")
            print(color.RED+color.BOLD +
                  "L'argomento che hai inserito è errato, prova di nuovo!"
                  + color.END)
    builtins.y = y
