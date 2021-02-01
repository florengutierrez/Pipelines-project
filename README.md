![IMDb](/images/IMDB.png)

### PIPELINE-PROJECT


En este proyecto realizo una pequeña limpieza de un dataset descargado de kaggle.com, y a través de la técnica de 

Web-scraping, extraigo información sobre "List of Academy Award-winning films". Sobre esto, lanzo un hipótesis:

#### ¿Están relacionadas las valoraciones de IMDb, con las películas ganadoras de premios Oscars?🎞

🎬 Guía del proyecto: 

- En functions.py(src) encontraremos las funciones de descarga del dataset, pequeña limpieza de este, y obtencion de tabla mediante Web-scraping.

- En merge.ipynb(src) nos encontramos con una pequeña limpieza de ambos dataframes(anteriormente obtenimos en functions.py), y      realizamos un merge de ambos.
Además obtendremos el top 10 de IMDb y de Academy Award-winning films.

- Por último en visualisation.ipynb(src) encontramos un par de gráficos donde podremos visualizar algunos aspectos sobre lo       trabajado.

Para complementar este proyecto, realizo mediante la API "OMDb API", una extracción de los posters de las películas mas relevantes vistas anteriormente.

#### Librerías 📚

- Pandas
- Numpy
- Seaborn
- Request
- Matplotlib


#### Links 🔗

"List of Academy Award-winning films" - https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films

"IMDb.csv" - https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset
