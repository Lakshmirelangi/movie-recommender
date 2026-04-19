import pandas as pd
from sklearn.neighbors import NearestNeighbors

def get_recommendations(user_id):
    df = pd.read_csv("movies.csv")

    user_movie_matrix = df.pivot(index='userId', columns='movieId', values='rating').fillna(0)

    model = NearestNeighbors(metric='cosine')
    model.fit(user_movie_matrix)

    target_user = user_movie_matrix.loc[user_id].values.reshape(1, -1)

    distances, indices = model.kneighbors(target_user, n_neighbors=3)

    similar_users = user_movie_matrix.index[indices.flatten()[1:]]

    recommendations = []

    for user in similar_users:
        movies = user_movie_matrix.loc[user]
        for movie, rating in movies.items():
            if rating >= 3 and user_movie_matrix.loc[user_id][movie] == 0:
                recommendations.append(movie)

    return list(set(recommendations))