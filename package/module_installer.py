import subprocess
import platform
import builtins
import importlib
import sys
import os


# Create a class to print colored text in the terminal
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


def modules(module_list):
    """Try to import needed modules.

       If module is not installed, it installs it.
    """
    status = 0
    builtins.status = 0
    for i in module_list:
        # Try to import a package
        try:
            globals()[i] = importlib.import_module(i)
        except ImportError:
            while True:
                # Prompt the user to download the needed modules
                print(color.CYAN + color.BOLD +
                      ("Il modulo %s non è presente nella tua libreria. Vuoi installarlo? [si/no]"
                       % (i))+color.END)
                scelta = str(input())
                if scelta in ["sì", "si", "Si", "SI"]:
                    subprocess.check_call([sys.executable,
                                           "-m", "pip", "install", i])
                    status = 0
                    builtins.status = 0
                    break
                if scelta in ["no", "No", "NO"]:
                    status = 1
                    builtins.status = 1
                    break
                else:
                    print("\n")
                    print(color.RED + color.BOLD +
                          "Hai inserito un parametro errato, prova di nuovo!" +
                          color.END)
        if status == 1:
            break
    if status == 1:
        print("\n")
        print(color.RED+color.BOLD +
              "Non riesco ad avviare il programma senza i pacchetti mancanti :(" +
              color.END)
