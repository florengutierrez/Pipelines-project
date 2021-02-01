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


  📜 Un poco de historia:

Los antecedentes de IMDb se remontan a 1989, cuando un aficionado publicó una discusión en un grupo de noticias en usenet sobre actrices atractivas. A partir de ese momento, otros usuarios de la lista comenzaron a recopilar actores y actrices con las películas en las que habían intervenido. La base de datos original fue construida a partir de las listas de créditos que Col Needham y otros dos lectores, Dave Knight y Andy Krieg, habían comenzado a publicar en el grupo. Needham publicó en septiembre de 1991 la primera herramienta simple (una serie de "shell scripts" de Unix) que permitía la consulta de las listas existentes en ese momento: la lista de directores, la de actores, la de actrices y la de actores fallecidos. Con la fusión de las cuatro la base de datos resultante se convertiría finalmente en la IMDb.