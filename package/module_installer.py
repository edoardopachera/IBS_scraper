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

       If module is not installed, this function installs it.
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
                # If input is positive, install package
                if scelta in ["sì", "si", "Si", "SI"]:
                    subprocess.check_call([sys.executable,
                                           "-m", "pip", "install", i])
                    status = 0
                    builtins.status = 0
                    break
                # If input is negative, don't install package
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
    # If the user refuses to download a package, the program stops
    if status == 1:
        print("\n")
        print(color.RED+color.BOLD +
              "Non riesco ad avviare il programma senza i pacchetti mancanti :(" +
              color.END)


def numpy_bug(package):
    """Correction of a Windows bug of numpy 1.19.4.

       Installs previous unbugged version (1.19.3).
    """
    for i in package:
        subprocess.check_call([sys.executable,
                              "-m", "pip", "install", "numpy==1.19.3"])


def check_install():
    """Modules download for different OS."""
    plt = platform.system()
    if plt == "Darwin":
        module_l = ["selenium", "bs4", "pyfiglet",
                    "argparse", "requests", "time",
                    "wikipedia", "pandas"]
    if plt == "Linux":
        module_l = ["selenium", "bs4", "pyfiglet",
                    "argparse", "requests", "time",
                    "wikipedia", "pandas"]
    if plt == "Windows":
        numpy_bug(['numpy'])
        module_l = ["selenium", "bs4", "pyfiglet",
                    "argparse", "requests", "time",
                    "wikipedia", "pandas", "win10toast"]

    modules(module_l)
