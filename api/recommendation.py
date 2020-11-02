import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import create_engine

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_genres(genres):
    return df[df.genres == genres]["index"].values[0]

def get_runtime_from_index(index):
    return df[df.index == index]["runtime"].values[0]
#Step 1: Read CSV File

engine = create_engine('mysql+pymysql://root:holymollybattlepass@localhost:3306/shimas')

dbConnection = engine.connect()

df = pd.read_sql("select * from movie_dataset", dbConnection)

# Step 2: Select Features
features = ['keywords', 'cast', 'genres', 'director']

#Step 3: Create a column in DF which combines all selected features
for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]

df["combined_features"] = df.apply(combine_features, axis=1)

#Step 4: Create count matrix from this new combined column
cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

#Step 5: Compute the Cosine Similiarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)

#Step 6: Get index of this movie from its title
def get_movie_recomendations(favorite, limit):
    movie_index = get_index_from_genres(favorite)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key= lambda x:x[1], reverse=True)
    recomendaciones = [] 
    i = 0
    for movie in sorted_similar_movies:
        recomendaciones.append({"title": get_title_from_index(movie[0]), "runtime": get_runtime_from_index(movie[0])})
        i += 1
        if i > limit:
            break

    return recomendaciones

dbConnection.close()