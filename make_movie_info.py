import latent_model as lm
import numpy as np
import pickle

movieData = np.loadtxt("movies.txt", delimiter='\t', dtype=bytes)
movieData = [[item.decode('utf-8') for item in row] for row in movieData]

users, movies, ratings = np.loadtxt("data.txt", unpack=True, dtype=int)

def projectMovies(N, M, Y):
    U, V, error = lm.train_model(M, N, 20, 0.02, 0.001, Y)

    a, s, b = np.linalg.svd(V, full_matrices=False)

    V_coords = np.dot(a[:2], V)
    U_coords = np.dot(a[:2], U.T)

    V_coords[0] /= np.max(np.abs(V_coords[0]))
    V_coords[1] /= np.max(np.abs(V_coords[1]))

    for i in range(N):
        movieInfo[i]['coords'] = (V_coords[0][i], V_coords[1][i])

def parseRatings():
    users, movies, _ = np.loadtxt("data.txt", unpack=True, dtype=int)
    M = np.max(users)
    N = np.max(movies)
    Y = np.loadtxt("data.txt", dtype=int)
    for _, j, y in Y:
        movieInfo[j-1]['ratings'].append(y)
    return N, M, Y

def parseMovie(label):
    categories =   ["Unknown", "Action", "Adventure", "Animation", "Childrens",
                    "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
                    "Film-Noir", "Horror", "Musical", "Mystery", "Romance",
                    "Sci-Fi", "Thriller", "War", "Western"]

    # format of movie object
    movie = {'title':'', 'year':0, 'genre':[], 'ratings':[]}

    # get movie title and year
    title = label[1].strip("\" ")
    movie['year'] = title[-6:].strip("()")
    title = title[:-6].strip()
    if title[-5:] == ", The":
        title = "The " + title[:-5]
    if title[-3:] == ", A":
        title = "A " + title[:-3]
    movie['title'] = title

    # get genres
    genres = label[-19:]
    for i, genre in enumerate(genres):
        if genre == "1":
            movie['genre'].append(categories[i])

    return movie

movieInfo = [parseMovie(label) for label in movieData]
N, M, Y = parseRatings()
projectMovies(N, M, Y)

with open('movie_info.pickle', 'wb') as handle:
    pickle.dump(movieInfo, handle)
