import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

def download_dataset():
    
   
    url = input("Introduce la url: ")
    
    
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]
    
    
    download = f"kaggle datasets download -d {user}/{endopint}; say -v Monica 'descargando'"
    decompress = f"tar -xzvf {endopint}.zip; say -v Monica 'descomprimiendo'"
    delete = f"rm -rf {endopint}.zip; say -v Monica 'borrando el zip'"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    
    lista_archivos = open('archivos.txt').read()
    nueva = lista_archivos.split("\n")
    
    
    for i in nueva:
        if i.endswith(".csv"):
            move_and_delete = f"mv {i} data/dataset.csv; rm archivos.txt; say -v Monica 'moviendo el dataset'"
            return os.system(move_and_delete)


def check_csv():
    
    df = pd.read_csv("../IMDb movies.csv", encoding = "latin-1")
    
    #remove columns
    df.drop(["imdb_title_id","metascore", "usa_gross_income",
             "budget", "worlwide_gross_income","reviews_from_critics",
             "reviews_from_users","votes","date_published","original_title",
             "production_company","language"], axis="columns", inplace=True)
    
    
    df.columns = df.columns.str.capitalize()
    # Eliminate rows that contain "NaN values" in all their columns.
      
    df.dropna(how='all')
    
    return df


def oscars():
    
    wiki_url = ("https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films")
    table_id = "wikitable sortable jquery-tablesorter"
    
    response = requests.get(wiki_url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    table=soup.find("table",{"class":"wikitable"})
   
    df=pd.read_html(str(table))
    # convert list to dataframe
    awards = pd.DataFrame(df[0])

    return awards
