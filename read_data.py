import numpy as np
import matplotlib.pyplot as plt

# dictionary of movies ids, containing containing {title, year, categories}
movieData = np.loadtxt("movies.txt", delimiter='\t', dtype=bytes)
movieData = [[item.decode() for item in row] for row in movieData]

users, movies, ratings = np.loadtxt("data.txt", unpack=True, dtype=int)

def parseRatings():
    n_users = len(set(users))
    n_movies = len(set(movies))
    R = [[0 for user in range(n_movies)] for movie in range(n_users)]
    for i in range(len(users)):
        R[users[i]-1][movies[i]-1] = ratings[i]
        movieInfo[movies[i]-1]['ratings'].append(ratings[i])

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
R = parseRatings()

def freqAll():
    n, bins, patches = plt.hist(ratings, bins=[1,2,3,4,5,6], align='left')
    plt.title("Distribution of Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.savefig('ratingsFreq.png')
    plt.clf()

    labels = ['1', '2', '3', '4', '5']
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', '#cc99ff']
    explode = (0, 0, 0, 0, 0)
    plt.pie(n, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=180)
    plt.axis('equal')
    plt.title("Distribution of Ratings", y=1.025)
    plt.savefig('ratingsPie.png')
    plt.clf()

def freqPopularBest():
    numRatings = []
    avgRatings = []

    for i in range(len(movieInfo)):
        numRatings.append(len(movieInfo[i]['ratings']))
        avgRatings.append(np.mean(movieInfo[i]['ratings']))

    popular = np.argsort(numRatings)[-10:]
    best = np.argsort(avgRatings)[-10:]

    return popular, best

popular, best = freqPopularBest()

def freqPopular():
    print("MOST POPULAR")
    for movie in popular:
        print(movieInfo[movie]['title'])

def freqBest():
    print("BEST RATED")
    for movie in best:
        print(movieInfo[movie]['title'], np.mean(movieInfo[movie]['ratings']), len(movieInfo[movie]['ratings']))

freqPopular()
freqBest()
