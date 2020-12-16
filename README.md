# IBS scraper :book:

This project is a website scraping terminal application. The target of the scraper is the <a href="https://www.ibs.it/" target="_blank">IBS</a> online bookstore. 
The main features of the program are: 
- A function that provides the user with a sorted list of book titles and corresponding authors from two sections of the website ('classifica della settimana' and 'consigliati').
- A function that allows the user to choose a book from the list and receive more information about it (plot, information about the author using Wikipedia's API and the price). 
- A function that allows the user to save his favorites books into a csv document stored into a specific folder.

## Requirements
- Google Chrome 86.0 or more recent versions
- **`python 3.7`** or more recent versions
- **`pip`**   command installed

## Installation 

### MacOS

<a href="https://imgbb.com/"><img src="https://i.ibb.co/nQxWkF1/Gif-Chromedriver.gif" alt="Gif-Chromedriver" border="0"></a> </br>
Check your Chrome version

1. Go to <a href="https://chromedriver.chromium.org/downloads" target="_blank">ChromeDriver</a> &rarr; download ChromeDriver for your Chrome version &rarr; download ChromeDriver for your OS.
   Move chromedriver inside the folder "chromedriver_settings".
2. Download the repository of the project from <a href="https://github.com/edoardopachera/IBS_scraper.git" target="_blank">GitHub</a>
   Click on the green button <b>Code</b>, then <b>Download Zip</b>. Once downloaded, decompress the Zip file.  
   MANCA GIF
3. Open the terminal and change your current directory into the downloaded repository.
  ```bash
   cd /path/to/my/repo
   ```    
 
### Linux

Follow the same steps above described. 

### Windows

Follow the same steps as described for MacOS.

<b>NOTE</b>: if the program stops beacuse of an error that returns "non-zero exit status 2", restart the program and it will work. 

## Run the program :keyboard:

1. Run the script by choosing between two mandatory arguments:
### MacOS
  ```bash
   python3 main.py consigliati
   ```
  ```bash
   python3 main.py classifica
   ```
### Windows
  ```bash
   py main.py consigliati
   ```
  ```bash
   py main.py classifica
   ```
2. Copy the directory of Chromdriver binary file and paste it in the command line.

For <b>Mac</b> add "/chromedriver" at the end of the directory.</br>
For<b>Windows</b> remember to remove the quotes from the directory before pasting it.</br>

3. The program checks if all the needed packages are installed in the computer. If some are missing, it will ask the user if to download them. 
4. Now, the program is ready and it will start!
   
## Menu parameters :clipboard:

The  **`argparse`** module allows the user to choose different options, other than the two mandatory classifica or consigliati:
1. **`help`** shows the two mandatory choices **`consigliati`** **`classifica`** 
2. **`-c`** or **`--csv`** displays the csv with the saved books
3. **`-r`** or **`--reset`** resets the csv with the saved books
4. **`-v`** or **`--verbose`** visualize the output with a human-friendly language
5. **`-q`** or **`--quiet`** visualizes a less human-friendly output 

## Team 

- [Edoardo Pachera](https://github.com/edoardopachera) 
- [Evita Jasinskaite](https://github.com/EvitaJasinskaite)
- [Leonardo Venturini](https://github.com/LeoVenturini)
- [Lorenzo Guetta](https://github.com/LGuetta)
- [Catalina Damian](https://github.com/catalina-damian)

## License
[MIT]
