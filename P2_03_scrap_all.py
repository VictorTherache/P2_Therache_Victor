
try:
    import requests
    import sys
    from bs4 import BeautifulSoup
    from P2_01_scrap_one_book import *
    from P2_02_scrap_one_category import *
    import csv
    import os.path
    from os import path
except ModuleNotFoundError as e:
    print("\nCertains modules sont manquants, veuillez taper"
          " 'pip install -r requirements.txt' pour les installer\n")
    raise SystemExit(e)


def get_categories_url(homepage_url):
    """
    Return an array of all categories urls
    """
    response = requests.get(homepage_url)
    if(response.ok):
        soup = BeautifulSoup(response.text, 'lxml')
        links = soup.find_all('a')
        categories_array = []
        for link in links:
            if "catalogue/category" in link['href']:
                categories_array.append("http://books.toscrape.com/" 
                + link['href'])
        return categories_array

def get_homepage_categories(homepage_url):
    """
    Return an array of all categories so the files can be checked
    """
    category_url = []
    response = requests.get(homepage_url, stream = True)
    soup = BeautifulSoup(response.text, 'lxml') 
    categories = soup.find('ul', {'class': 'nav-list'})
    categories = categories.find_all('a')
    for category in categories:
        category_url.append(category.text.strip())
    return category_url


def scrap_all_books(homepage_url):
    """
    Puts all the books informations from the website in multiple csvs
    """
    categories_urls = get_categories_url(homepage_url)
    categories_urls.pop(0)
    for category in categories_urls:
        put_books_info_in_csv(category)


if __name__ == '__main__':
    try:
        homepage_url = "https://books.toscrape.com/"
        categories_array = get_homepage_categories(homepage_url)
        for category in categories_array:
            check_files(category)
        scrap_all_books(homepage_url)
        print('\n**** Success ****\n')
    except requests.exceptions.RequestException as e: 
        print("\nErreur de connection, veuillez vérifier" 
              " votre connection internet ou rentrer un url valide\n")
        raise SystemExit(e)
