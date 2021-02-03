# P2_Therache_Victor
## Table des matières
1. [Information générale](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)

### Information générale
***
Ce petit programme codé en python vous permettra de scraper la totalité de la bibliothèque du site https://books.toscrape.com/ avec la possibilité de récuperer les informations d'un livre, de toute une catégorie ou du site entier.
### Screenshot
![Image text](https://i.ibb.co/LC80vpd/banniere-op.png)
## Technologies
***
Technologie utilisé :
* [Python 64bit](https://www.python.org/downloads/release/python-391/): Version 3.9.1
* [sys](https://docs.python.org/fr/3/library/sys.html)
* [requests](https://requests.readthedocs.io/en/master/): Version 2.25.0
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Version 4.9.3
* [os.path](https://docs.python.org/3/library/os.path.html)
* [lxml](https://lxml.de/installation.html): Version 4.6.1

## Installation
***
Pour installer le programme, entrez ces commandes dans un terminal :
```
Sur Windows : 
$ git clone https://github.com/VictorTherache/P2_Therache_Victor.git
$ cd P2_Therache_Victor/
$ pip3 install -r requirements.txt 
$ py P2_01_scrap_one_book https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
  or py P2_02_scrap_one_cateogory https://books.toscrape.com/catalogue/category/books/poetry_23/index.html
  or py P2_03_scrap_all.py
```
```
Sur Linux/Mac : 
$ git clone https://github.com/VictorTherache/P2_Therache_Victor.git
$ cd P2_Therache_Victor/
$ pip3 install -r requirements.txt 
$ python P2_01_scrap_one_book https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
  or python P2_02_scrap_one_cateogory https://books.toscrape.com/catalogue/category/books/poetry_23/index.html
  or python P2_03_scrap_all.py
```
Merci d'avoir téléchargé ce projet :) 
