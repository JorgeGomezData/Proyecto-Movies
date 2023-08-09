from fastapi import FastAPI
import pandas as pd

app = FastAPI()

movies_cleaned=pd.read_csv('/Users/user/Library/Mobile Documents/com~apple~CloudDocs/Henry/Proyecto Individual/movies_cleaned.csv')

@app.get('/peliculas_idioma/{Idioma}')
def peliculas_idioma(Idioma: str):
    # Filtrar el DataFrame por el idioma especificado
    peliculas_filtradas = movies_cleaned[movies_cleaned['original_language'] == Idioma]

    # Obtener la cantidad de películas en el idioma especificado
    cantidad_peliculas = peliculas_filtradas.shape[0]

    return f"{cantidad_peliculas} cantidad de películas fueron estrenadas en idioma '{Idioma}'."
     
@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(Pelicula: str):
    # Filtrar el DataFrame para obtener la fila correspondiente a la película
    pelicula_filtrada = movies_cleaned[movies_cleaned['title'] == Pelicula]

    # Verificar si la película existe en el DataFrame
    if pelicula_filtrada.empty:
        return "La película no fue encontrada en el dataset."

    # Obtener la duración y el año de lanzamiento
    duracion = pelicula_filtrada['runtime'].values[0]
    anio = pelicula_filtrada['release_year'].values[0]

    # Retornar el mensaje con la duración y el año
    return f"{Pelicula}. Duración: {duracion}. Año: {anio}" 

@app.get('/franquicia/{franquicia}')
def franquicia(Franquicia: str):
    franquicia_data = movies_cleaned[movies_cleaned['belongs_to_collection'] == Franquicia]

    cantidad_peliculas = franquicia_data.shape[0]
    ganancia_total = franquicia_data['revenue'].sum()
    ganancia_promedio = ganancia_total / cantidad_peliculas

    mensaje_retorno = f"La franquicia {Franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total:.2f} y una ganancia promedio de {ganancia_promedio:.2f}"
    return mensaje_retorno

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(Pais: str):
    cantidad_peliculas = movies_cleaned['production_countries'].str.contains(Pais).sum()
    mensaje_retorno = f"Se produjeron {cantidad_peliculas} películas en el país {Pais}"
    return mensaje_retorno

@app.get('/productoras_exitosas/{Productora}')
def productoras_exitosas(Productora: str):
    # Llenar los valores NaN en la columna 'production_companies' con una cadena vacía ('')
    movies_cleaned['production_companies'] = movies_cleaned['production_companies'].fillna('')

    productora_data = movies_cleaned[movies_cleaned['production_companies'].str.contains(Productora)]

    cantidad_peliculas = productora_data.shape[0]
    revenue_total = productora_data['revenue'].sum()

    mensaje_retorno = f"La productora {Productora} ha tenido un revenue de {revenue_total:.2f} en {cantidad_peliculas} películas"
    return mensaje_retorno

@app.get('/get_director/')
def get_director(nombre_director: str):
    resultado = []
    director_data = movies_cleaned[movies_cleaned['crew'] == nombre_director]
    
    if not director_data.empty:
        total_return = director_data['return'].sum()  # Calculate total return
        for _, row in director_data.iterrows():
            pelicula_info = {
                "nombre_pelicula": row['title'],
                "fecha_lanzamiento": row['release_date'],
                "retorno_individual": row['return'],
                "costo": row['budget'],
                "ganancia": row['revenue']
            }
            resultado.append(pelicula_info)
        return {
            "director": nombre_director,
            "exito": total_return,
            "peliculas": resultado
        }
    else:
        return {"message": "El director no se encuentra en el dataset"}

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



# Crear un vectorizador CountVectorizer para los títulos de las películas
count_vectorizer = CountVectorizer(stop_words='english')
count_matrix = count_vectorizer.fit_transform(movies_cleaned['title'])

# Calcular la similitud del coseno entre las películas
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# Crear un diccionario que mapee los títulos de las películas con sus índices en el DataFrame
indices = pd.Series(movies_cleaned.index, index=movies_cleaned['title']).drop_duplicates()

@app.get('/recomendacion/{Titulo}')
def recomendacion(titulo):
    # Obtener el índice de la película ingresada
    idx = indices[titulo]

    # Calcular la similitud del coseno para todas las películas
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Ordenar las películas según la similitud en orden descendente
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Obtener los índices de las 5 películas más similares (excluyendo la película ingresada)
    top_indices = [i[0] for i in sim_scores[1:6]]

    # Obtener los títulos de las 5 películas más similares
    top_titles = movies_cleaned['title'].iloc[top_indices].tolist()

    return top_titles



