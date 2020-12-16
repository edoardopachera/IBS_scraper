import subprocess
import platform
import builtins
import importlib
import sys
import os


# Create a class to print colored text in the terminal
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
            subprocess.check_call([sys.executable, "-m", "pip", "install", i])


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
