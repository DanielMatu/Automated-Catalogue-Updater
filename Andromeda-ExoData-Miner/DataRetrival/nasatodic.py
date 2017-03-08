# note: need to download modules "requests" and "BeautifulSoup" to work
import requests
from bs4 import BeautifulSoup


def crawler(main_url="http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets"):
    '''
    String -> Dictionary{tag : list of strings}
    Crawls a catalog url and generates the corresponding dictionary
    '''
    source_code = requests.get(main_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    nasa_dict = {}
    # split the string into a list of rows
    rows = plain_text.split('\n')
    # split each row by comma
    for i in range(len(rows)):
        rows[i] = rows[i].split(',')
    # initialize each tag to an empty list
    for j in range(len(rows[0])):
        nasa_dict[rows[0][j]] = []
    # iterate through every non-tag entry and map
    for i in range(len(rows) - 2):
        for j in range(len(rows[i])):
            nasa_dict[rows[0][j]].append(rows[i + 1][j])
    return nasa_dict

