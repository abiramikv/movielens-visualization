import matplotlib.pyplot as plt
import numpy as np
import pickle

with open('movie_info.pickle', 'rb') as handle:
    movieInfo = pickle.load(handle)

random = [0, 120, 255, 49, 21, 1479, 1469, 1, 1273, 448]
popular = np.argsort([len(movie['ratings']) for movie in movieInfo])[-10:]
best = np.argsort([np.mean(movie['ratings']) for movie in movieInfo])[-10:]
dramas = [i for i, m in enumerate(movieInfo) if "Drama" in m["genre"]]
horrors = [i for i, m in enumerate(movieInfo) if "Horror" in m["genre"]]
actions = [i for i, m in enumerate(movieInfo) if "Action" in m["genre"]]


def makeScatter(movies, filename, title):
    x = [movieInfo[i]["coords"][0] for i in movies]
    y = [movieInfo[i]["coords"][1] for i in movies]

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_title("Latent Factor Visualation for " + title)
    ax.scatter(x, y)
    for i, j in enumerate(movies):
        ax.annotate(movieInfo[j]["title"], (x[i] + 0.015, y[i] - 0.015))
    fig.savefig("img/" + filename)
    fig.clf()

def part1():
    pass

def part2():
    makeScatter(random, "random_scatter.png", "10 Random Movies")
    makeScatter(popular, "popular_scatter.png", "10 Most Popular Movies")
    makeScatter(best, "best_scatter.png", "10 Highest Rated Movies")
    makeScatter(dramas[:10], "drama_scatter.png", "10 Drama Movies")
    makeScatter(horrors[:10], "horror_scatter.png", "10 Horror Movies")
    makeScatter(actions[:10], "action_scatter.png", "10 Action Movies")

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

def freqPopular():
    numRatings = []
    for movie in popular:
        numRatings.append(movieInfo[movie]['ratings'])

    plt.hist(numRatings, bins=[1,2,3,4,5,6], align='left', stacked=True)
    plt.title("Distribution of Ratings for Most Popular Movies")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.savefig('popularFreq.png')
    plt.clf()

def freqBest():
    print("BEST RATED")
    for movie in best:
        print(movieInfo[movie]['title'], np.mean(movieInfo[movie]['ratings']), len(movieInfo[movie]['ratings']))

freqPopular()
freqBest()

part1() and part2()
