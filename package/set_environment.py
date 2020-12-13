from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pyfiglet
import os


# Class to print colored text in terminal
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


def opening_logo():
    """Displays an ascii logo of IBS Scraper"""
    word = pyfiglet.figlet_format("IBS Scraper")
    print(word)


def directory_checks():
    """Define the chromedriver path variable"""
    global CHROMEDRIVER_PATH
    # Create a folder for the chromedriver
    # directory storage file
    try:
        os.mkdir("%s/chromedriver_settings" % (os.getcwd()))
    except:
        pass
    try:
        with open(("%s/chromedriver_settings/chromedriver_dir.txt"
                  % (os.getcwd())), 'r+') as c:
            first_line = c.readline()
            # If the directory isn't written in the file
            if first_line == '':
                print((color.BOLD
                      + "Non è possibile avviare il programma: "+color.END)
                      + (color.CYAN+color.BOLD
                      + "Copia e incolla qui sotto la directory del file chromedriver"
                      + color.END))
                directory = input()
                c.write(directory)
                status = 1
            else:
                CHROMEDRIVER_PATH = str(first_line)
                status = 2
        if status == 1:
            with open(("%s/chromedriver_settings/chromedriver_dir.txt"
                      % (os.getcwd())), 'r+') as n:
                CHROMEDRIVER_PATH = str(n.readline())
    except IOError:
        try:
            os.mkdir("%s/chromedriver_settings" % (os.getcwd()))
        except:
            pass
        print(color.RED+color.BOLD
              + "Il file 'chromedriver_dir.txt' non esiste, lo creo io per te"
              + color.END)
        with open(("%s/chromedriver_settings/chromedriver_dir.txt"
                  % (os.getcwd())), 'w') as file:
            print(color.CYAN+color.BOLD
                  + "Copia e incolla qui sotto la directory del file chromedriver"
                  + color.END)
            directory = input()
            file.write(directory)
        with open(("%s/chromedriver_settings/chromedriver_dir.txt"
                   % (os.getcwd())), 'r') as c:
            first_line = c.readline()
            CHROMEDRIVER_PATH = str(first_line)
        pass


def chrome_options():
    """Define selenium browser.

       Set options to run in background.
    """
    global browser
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                               options=chrome_options)
