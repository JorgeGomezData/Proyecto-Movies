
![Logo Henry](logoHenry.png)
# Proyecto Individual Henry Bootcamp
Sistema de Recomendaciones de Películas.


## Objetivo
Crear un modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha!
## Descripción del Proyecto
El proyecto hace parte del componente de proyectos individuales del Bootcamp en Datascience realizado en la academia Henry durante al año 2023.
Consiste en la creación de un primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha en una start-up que provee servicios de agregación de plataformas de streaming.

En ese sentido en una primera indagación sobre los datos provistos, se puede inferir que  madurez de los mismos es poca: Datos anidados, sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas.

Para lo cual, se realizará el desanidado de las columnas en donde los valores se encuentren como listas o listas de diccionarios, también se realizará el borrado (drop)de las columnas de los datasets provistos que puede no ser útiles para la creación del modelo ML, luego se construyen las funcionalidades a las cuales los usuarios podrán tener acceso en una API alojada en la web.


## Estado del Proyecto
Para fines académico el proyecto se debe realizar hasta la creación del modelo de ML de recomendación de peliculas basado en la puntuación que los usuarios le han dado a las mismas, sin embargo se puede considerar aún, un proyecto en construcción. 

### ETL
Dentro del proceso de ETL de los datos se desarrollaron las siguientes funciones con las cuales se logró principalmente el desanidado de los valores en las columnas que estaban en dicccionarios o listas. 

### Función para desanidar la columna 'belongs_to_collection'
def extraer_collection_name(collection):
    if pd.isnull(collection):
        return np.nan
    else:
        try:
            return ast.literal_eval(collection)['name']
        except (ValueError, TypeError):
            return np.nan


## Funcionalidades del Proyecto

|Nombre Función| Descripción|Retorno |
|--------------|------------|--------|
|def peliculas_idoma( Idioma: str )|Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!).|X cantidad de películas fueron estrenadas en idioma
|def peliculas_duracion( Pelicula: str )| Se ingresa una pelicula.|X . Duración: x. Año: xx|
|def franquicia( Franquicia: str )| Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio|La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx|
def peliculas_pais( Pais: str )| Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!)|Ejemplo de retorno: Se produjeron X películas en el país X
|def productoras_exitosas( Productora: str )| Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo. |Ejemplo de retorno: La productora X ha tenido un revenue de x|
def get_director( nombre_director )|Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno.| Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

Igualmente dentro de las funcionalidades se encuentra el sistema de recomendaciones de las películas, realizado con Machine Learning

## Acceso
Los usuarios pueden tener acceso a la API a través del link *localhost:8000/docs* en su navegador

## Librerias utilizadas
El proyecto utiliza las siguientes librearias de Python
- Pandas
- Sklearn
- Numpy
- FastAPI

## Autor
Jorge Gómez






