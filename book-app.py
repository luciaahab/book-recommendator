
#bibliotecas

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

import seaborn as sns
%matplotlib inline

from io import BytesIO





# This app gives book recommendations

def recomendaciones(title,cosine_sim=cosine_sim ):
    idx = indices[title]    #índices de los libros que concuerde con el titulo
    
    sim_scores = list(enumerate(cosine_sim[idx])) #similaridad entre scores de todas las películas con 1
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)   #clasifica los libros basándose en el score de similiridad
    sim_scores = sim_scores[1:6]   #6 de las mejores. Con esto se puede ajustar el nº de recomendaciones
    
    lib_indices = [i[0] for i in sim_scores]    #consigue los índices de los libros
    
    
    
    
    
    
    # Esto para las imágenes   
    # taking the title and book image link and store in new data frame called books
    books = libros[['title', 'image_link']]
    #Reverse mapping of the index
    recommend = books.iloc[indices]
    
    book_indices = [i[0] for i in sim_scores]
    recommend = books.iloc[book_indices]

    
    for index, row in recommend.iterrows():

        response = requests.get(row['image_link'])
        img = Image.open(BytesIO(response.content))
        plt.figure()
        plt.imshow(img)
        plt.title(row['title'])
    
    
    
    
    
    return libros['title'].iloc[lib_indices]   #devuelve
    
    
    
    
    

