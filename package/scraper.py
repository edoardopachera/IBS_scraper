from bs4 import BeautifulSoup
import platform
import wikipedia
import builtins
import time


class color:
    plt = platform.system()
    if plt == "Darwin":
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
    if plt == "Windows":
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERLINE = ''
        END = ''
    if plt == "Linux":
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
    """Uses the selenium browser to navigate to an inputed link.

    Saves the html into a BeautifulSoup object.
    """
    browser = builtins.browser
    browser.get(link)
    time.sleep(2)
    content = browser.page_source.encode('utf-8').strip()
    global soup
    soup = BeautifulSoup(content, "html.parser")


def consigliati_scraper():
    """Returns a list with recommended books.

    Allows the user to get more info about a single book.
    """
    global book_dict
    global scelta
    global price
    print("\n")
    if builtins.args.type == "v":
        print(color.CYAN + color.BOLD +
              "Sto caricando i libri consigliati della settimana..."
              + color.END)
    if builtins.args.type == "q":
        print(color.CYAN + color.BOLD +
              "Caricamento consigliati in corso..."
              + color.END)
    navigate_to_soup('https://www.ibs.it/libri-consigliati-da-leggere')
    # Inspect the html
    main = soup.find(
        "div",
        {"class": "modulo-ctn mdl-listaprodotti padding-sp padding-top"})
    sections = main.findAll("div", {"class": "box-body"})
    book_dict = {}
    index = 1
    print("\n")
    if builtins.args.type == "v":
        print(color.BOLD + "Ecco qui:" + color.END)
    # Scrape important attributes in each section
    for section in sections:
        book_name = section.find("h5", {"class": "subtitle"}).text.strip()
        author_container = section.find("div", {"class": "box-title-prd"})
        author = author_container.h3.text.strip()
        plot_container = section.find("div", {"class": "abstract"})
        plot = plot_container.p.text.strip()
        link = ("https://www.ibs.it"+section.figure.a['href'])
        book_info = [author, book_name, plot, link]
        # Save the collected info into a dictionary
        book_dict[index] = book_info
        print(str(index)+". "+book_name+"  ("+author+")")
        index += 1
    print("\n")
    builtins.book_dict = book_dict
    # Whitelist correct inputs
    while True:
        # If verbose
        if builtins.args.type == "v":
            print(color.BOLD +
                  "Di quale libro vuoi avere più informazioni? (Inserire numero)"
                  + color.END)
        # If quiet
        if builtins.args.type == "q":
            print(color.BOLD + "Inserire numero libro:" + color.END)
        scelta = input()
        try:
            scelta = int(scelta)
            # If scelta is an integer between the first and the last book
            if isinstance(scelta, int) is True and scelta in range(1, index):
                builtins.scelta = scelta
                break
            else:
                print("\n")
                if builtins.args.type == "v":
                    print(color.BOLD + color.RED +
                          "Hai inserito un valore errato, prova di nuovo!"
                          + color.END)
                if builtins.args.type == "q":
                    print(color.BOLD + color.RED +
                          "Prova di nuovo!"
                          + color.END)
        except ValueError:
            print("\n")
            if builtins.args.type == "v":
                print(color.BOLD + color.RED +
                      "Hai inserito un valore errato, prova di nuovo!"
                      + color.END)
            if builtins.args.type == "q":
                print(color.BOLD + color.RED+"Prova di nuovo!"+color.END)
    # Assign info to different variables
    libro_scelto = book_dict.get(scelta, None)
    autore_libro_scelto = libro_scelto[0]
    nome_libro_scelto = libro_scelto[1]
    link_libro_scelto = libro_scelto[3]
    plot_libro_scelto = libro_scelto[2]
    print("\n")
    if builtins.args.type == "v":
        print("Hai scelto: " +
              (color.PURPLE + color.BOLD + '"' + color.END) +
              (color.PURPLE +
               color.BOLD + "%s" + color.END) % (nome_libro_scelto) +
              (color.PURPLE + color.BOLD + '"' + color.END))
    if builtins.args.type == "q":
        print(
              (color.PURPLE +
               color.BOLD + "%s" + color.END) % (nome_libro_scelto))
    navigate_to_soup(link_libro_scelto)

    price = soup.find(
        "h2", {"data-aid": "pdp_price_current-price"}).text.strip()
    builtins.price = price
    # Use the wikipedia API to get more info about the author
    wikipedia.set_lang("it")
    try:
        about_the_author = wikipedia.summary(autore_libro_scelto, sentences=1)
    except:
        if builtins.args.type == "v":
            about_the_author = "Non sono presenti info su questo autore :("
        if builtins.args.type == "q":
            about_the_author = "No info"
    print("\n")
    if builtins.args.type == "v":
        print(color.BOLD + "Ecco maggiori info:" + color.END)
    print("\n")
    # Display info
    print((color.DARKCYAN+color.BOLD + "AUTORE:  " +
           color.END)+autore_libro_scelto.upper())
    print(about_the_author)
    print("\n")
    print((color.DARKCYAN+color.BOLD + "PREZZO:  "+color.END)+price)
    print("\n")
    print((color.DARKCYAN+color.BOLD + "TRAMA:  "+color.END)+plot_libro_scelto)
    time.sleep(3)
    print("\n")
    (builtins.browser).quit()


def classifica_scraper():
    """Returns a list of the week best sellers.

    Allows the user to have more information about a single book.
    """
    global book_dict
    global scelta
    # If verbose
    if builtins.args.type == "v":
        print(color.CYAN+color.BOLD +
              "Sto caricando i libri in classifica questa settimana..." +
              color.END)
        print(color.BOLD + color.YELLOW +
              "Potrebbero volerci alcuni minuti in base alla tua connessione internet"
              + color.END)
    # If quiet
    if builtins.args.type == "q":
        print(color.CYAN + color.BOLD +
              "Caricamento classifica in corso..."
              + color.END)

    try:
        # If the book info dictionary is full,
        # the script is not in the first run
        if builtins.book_dict != {}:
            for i in builtins.book_dict:
                print(str(i) + ". " +
                      ((builtins.book_dict[i])[1]) +
                      "  ("+((builtins.book_dict[i])[0]) +
                      ")")
    except NameError and AttributeError:
        # If the book info dictionary is empty, the script is in the first run
        # Start scraping info
        navigate_to_soup('https://www.ibs.it/classifica/libri/1week/sold?defaultPage=1')
        main = soup.find("div",
                         {"class":
                          "col-lg-25 col-md-25 col-sm-25 col-xs-25 gridContainer"})
        sections = main.findAll("li",
                                {"class":
                                 "col-lg-5 col-md-5 col-sm-25 col-xs-25"})
        book_dict = {}
        index = 1
        print("\n")
        if builtins.args.type == "v":
            print(color.BOLD + "Ecco qui:" + color.END)
        # Scrape important attributes in each section
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
            # Save the collected info into a dictionary
            book_dict[index] = book_info
            print(str(index)+". "+book_name+"  ("+author+")")
            index += 1
        builtins.book_dict = book_dict
        builtins.index = index
    print("\n")
    # Whitelist correct inputs
    while True:
        if builtins.args.type == "v":
            print(color.BOLD +
                  "Di quale libro vuoi avere più informazioni? (Inserire numero)"
                  + color.END)
        if builtins.args.type == "q":
            print(color.BOLD + "Inserire numero libro:" + color.END)
        scelta = input()
        try:
            scelta = int(scelta)
            if isinstance(scelta, int) is True and scelta in range(1, builtins.index):
                builtins.scelta = scelta
                break
            else:
                print("\n")
                if builtins.args.type == "v":
                    print(color.BOLD + color.RED +
                          "Hai inserito un valore errato, prova di nuovo!" +
                          color.END)
                if builtins.args.type == "q":
                    print(color.BOLD + color.RED+"Prova di nuovo!"+color.END)
        except ValueError:
            print("\n")
            if builtins.args.type == "v":
                print(color.BOLD + color.RED +
                      "Hai inserito un valore errato, prova di nuovo!" +
                      color.END)
            if builtins.args.type == "q":
                print(color.BOLD + color.RED + "Prova di nuovo!" + color.END)
    # Assign a variable for each info
    libro_scelto = book_dict.get(scelta, None)
    libro_scelto = book_dict.get(scelta, None)
    autore_libro_scelto = libro_scelto[0]
    nome_libro_scelto = libro_scelto[1]
    link_libro_scelto = libro_scelto[3]
    plot_libro_scelto = libro_scelto[2]
    price_libro_scelto = libro_scelto[4]
    builtins.price = price_libro_scelto
    print("\n")
    if builtins.args.type == "v":
        print("Hai scelto: " + (color.PURPLE +
              color.BOLD + '"' + color.END) +
              (color.PURPLE + color.BOLD + "%s" +
              color.END) % (nome_libro_scelto) +
              (color.PURPLE + color.BOLD + '"' +
              color.END))
    if builtins.args.type == "q":
        print((color.PURPLE + color.BOLD +
              "%s" + color.END) % (nome_libro_scelto))

    # Use the Wikipedia API to get more info about the author
    wikipedia.set_lang("it")
    try:
        about_the_author = wikipedia.summary(autore_libro_scelto, sentences=1)
    except:
        if builtins.args.type == "v":
            about_the_author = "Non sono presenti info su questo autore :("
        if builtins.args.type == "q":
            about_the_author = "No info"
    print("\n")
    if builtins.args.type == "v":
        print(color.BOLD + "Ecco maggiori info:" + color.END)
        print("\n")
        # Display the book info
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
    (builtins.browser).quit()


def recursive():
    """Restarts the scraper if the user wants to."""
    global y
    y = 1
    while True:
        print("\n")
        print(color.BOLD+"Vuoi avere info su altri libri? [si/no]"+color.END)
        scelta = str(input())
        if scelta in ["sì", "si", "Si", "SI"]:
            # If the user wants to continue, y = 1
            y = 1
            print("\n")
            break
        elif scelta in ["no", "No", "NO"]:
            # If the user does not want to continue, y = 2
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
