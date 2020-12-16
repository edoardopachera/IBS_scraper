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
