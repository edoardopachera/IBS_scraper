import package.module_installer as mi
import builtins
import argparse
import textwrap

# ARGPARSE
parser = argparse.ArgumentParser(prog='main.py',
                                 description='''Guida IBS Scraper: Questo
                                                programma naviga sul sito
                                                IBS.it e scarica le
                                                informazioni più importanti
                                                delle pagine
                                                "libri consigliati
                                                della settimana" e "libri
                                                in classifica questa
                                                settimana".
                                                Hai la possibilità di
                                                scegliere da quale
                                                delle due categorie
                                                ricevere le informazioni,
                                                e di salvare in una lista
                                                csv i libri che ti
                                                interessano di più.
                                            ''')
# Positional Arguments
parser.add_argument("tipo_di_lista",
                    help='scegli il tipo di lista dei libri tra [consigliati | classifica]',
                    choices=["consigliati", "classifica"], type=str)
# Optional Arguments
parser.add_argument('-c', '--csv', action='store_true',
                    help='visualizza csv dopo aver salvato un libro')
parser.add_argument('-r', '--reset', action='store_true',
                    help='resetta la lista dei libri salvati')
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_const', dest='type',
                   const='v',
                   help='visualizza output con testo più human friendly')
group.add_argument('-q', '--quiet', action='store_const', dest='type',
                   const='q', help='visualizza output diretto con meno testo')
parser.set_defaults(type='v')
args = parser.parse_args()
builtins.args = args


# PROGRAM EXECUTION
if __name__ == '__main__':
    # Endless cycle, until function "recursive" stops it
    while True:
        # Check the installation of packages
        mi.check_install()
        # If the user refused to install a needed package
        # stop the program
        if builtins.status == 1:
            break
        if args.tipo_di_lista == "consigliati":
            import package.set_environment as se
            import package.scraper as sc
            import package.book_saver as bs
            se.opening_logo()
            se.directory_checks()
            while True:
                se.chrome_options()
                CHROMEDRIVER_PATH = se.CHROMEDRIVER_PATH
                builtins.browser = se.browser
                # Run the scraper
                sc.consigliati_scraper()
                book_dict = builtins.book_dict
                scelta = builtins.scelta
                price = builtins.price
                bs.save_book(book_dict, scelta)
                sc.recursive()
                # If the user says "No" to "recursive" function
                # stop the program
                if builtins.y == 2:
                    print("\n")
                    break
            break
        elif args.tipo_di_lista == "classifica":
            import package.set_environment as se
            import package.scraper as sc
            import package.book_saver as bs
            se.opening_logo()
            se.directory_checks()
            while True:
                se.chrome_options()
                CHROMEDRIVER_PATH = se.CHROMEDRIVER_PATH
                builtins.browser = se.browser
                # Run the scraper
                sc.classifica_scraper()
                book_dict = builtins.book_dict
                scelta = builtins.scelta
                bs.save_book(book_dict, scelta)
                sc.recursive()
                # If the user says "No" to "recursive" function
                # stop the program
                if builtins.y == 2:
                    print("\n")
                    break
            break
