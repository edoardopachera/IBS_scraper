import pandas as pd
import builtins
import platform
import time
import os

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


def notification(title, message):
    """Sends a notification when the book is saved."""
    plt = platform.system()
    # If OS is MacOS
    if plt == 'Darwin':
        command = f'''
        osascript -e 'display notification "{message}" with title "{title}"'
        '''
        os.system(command)
    # If OS is Linux
    if plt == 'Linux':
        command = f'''
        notify-send "{title}" "{message}"
        '''
        os.system(command)
    # If OS is Windows
    if plt == 'Windows':
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(("%s" % (title)), ("%s" % (message)))


def save_book(book_dict, book_index):
    """Asks the user to save the book.
    
       Save the book into a csv file.
    """
    args = builtins.args
    price = builtins.price
    # If optional argument is --reset 
    # the csv is cleared before adding the new book
    if args.reset:
        try:
            os.remove("%s/csv/libri_salvati.csv" % (os.getcwd()))
        except:
            pass
    while True:
        # If --verbose
        if builtins.args.type == "v":
            print(color.BOLD +
                  "Vuoi salvare questo libro nella tua lista? [si/no]"
                  + color.END)
        # If --quiet
        if builtins.args.type == "q":
            print(color.BOLD+"Aggiungere al csv? [si/no]"+color.END)
        scelta = str(input())
        if scelta in ["sì", "si", "Si", "SI"]:
            print("\n")
            try:
                # Read the csv
                salvati_csv = pd.read_csv("%s/csv/libri_salvati.csv"
                                          % (os.getcwd()),
                                          encoding="utf-8")
                # Source is the chosen book value in the dictionary
                source = book_dict[book_index]
                if args.tipo_di_lista == "consigliati":
                    pr = price
                if args.tipo_di_lista == "classifica":
                    pr = source[4]
                to_append = [source[0], source[1], pr, source[3]]
                salvati_csv_length = len(salvati_csv)
                salvati_csv.loc[salvati_csv_length] = to_append
                # Remove the old csv
                os.remove("%s/csv/libri_salvati.csv" % (os.getcwd()))
                # Create a csv with the new book
                salvati_csv.to_csv("%s/csv/libri_salvati.csv" % (os.getcwd()),
                                   index=False, header=True)
                notification("IBS Scraper",
                             ("Hai salvato con successo %s nella tua lista dei preferiti"
                              % (source[1])))
                if args.csv:
                    print(color.DARKCYAN+color.BOLD +
                          "Ecco la tua lista:"
                          + color.END)
                    print(salvati_csv)
            except:
                # Create csv folder
                try:
                    os.mkdir("%s/csv" % (os.getcwd()))
                except:
                    pass
                source = book_dict[book_index]
                if args.tipo_di_lista == "consigliati":
                    pr = price
                if args.tipo_di_lista == "classifica":
                    pr = source[4]
                data = {'Autore':  [source[0]],
                        'Libro': [source[1]],
                        'Prezzo': [pr],
                        'Link': [source[3]]}
                # Create a dataframe with selected columns
                salvati_csv = pd.DataFrame(data,
                                           columns=['Autore', 'Libro',
                                                    'Prezzo', 'Link'])
                salvati_csv.to_csv(("%s/csv/libri_salvati.csv"
                                    % (os.getcwd())),
                                   index=False, header=True)
                notification("IBS Scraper",
                             ("Hai salvato con successo %s nella tua lista dei preferiti"
                              % (source[1])))
                if args.csv:
                    print(color.DARKCYAN+color.BOLD +
                          "Ecco la tua lista:"
                          + color.END)
                    print(salvati_csv)
                break
            break
        # If the user chooses not to save the book
        elif scelta in ["no", "No", "NO"]:
            print("\n")
            if builtins.args.type == "v":
                print(color.BOLD +
                      "Va bene! Non ho salvato questo libro"
                      + color.END)
            if args.csv:
                # Try to open the csv
                try:
                    salvati_csv = pd.read_csv("%s/csv/libri_salvati.csv"
                                              % (os.getcwd()),
                                              encoding="utf-8")
                # Except csv not existing
                except:
                    salvati_csv = (color.BOLD +
                                   color.RED +
                                   "Non è stata trovata alcuna lista dei preferiti"
                                   + color.END)
                print(color.DARKCYAN+color.BOLD+"Ecco la tua lista:"+color.END)
                print(salvati_csv)
            break
        else:
            print("\n")
            if builtins.args.type == "v":
                print(color.RED +
                      color.BOLD +
                      "L'argomento che hai inserito è errato, prova di nuovo!"
                      + color.END)
            if builtins.args.type == "q":
                print(color.RED+color.BOLD+"Prova di nuovo!"+color.END)
