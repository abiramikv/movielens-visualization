import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import seaborn as sns

with open('data/movie_info.pickle', 'rb') as handle:
    movieInfo = pickle.load(handle)

every = range(len(movieInfo))
random = [0, 120, 255, 49, 21, 1479, 1469, 1, 1273, 448]
popular = np.argsort([len(movie['ratings']) for movie in movieInfo])[-10:]
best = np.argsort([np.mean(movie['ratings']) for movie in movieInfo])[-10:]
dramas = [i for i, m in enumerate(movieInfo) if "Drama" in m["genre"]]
horrors = [i for i, m in enumerate(movieInfo) if "Horror" in m["genre"]]
actions = [i for i, m in enumerate(movieInfo) if "Action" in m["genre"]]

def makeHistogram(movies, filename, title, aggregate=True):
    ratings = []
    titles = []
    for i in movies:
        for rating in movieInfo[i]["ratings"]:
            ratings.append(rating)
            titles.append(movieInfo[i]["title"])

    data = {'ratings' : ratings, 'titles' : titles}

    fig, ax = plt.subplots()

    if aggregate:
        ax = sns.countplot(data=data, x='ratings')
        ax.set_xlabel("Rating")
    else:
        ax = sns.countplot(data=data, x='titles', hue='ratings')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        ax.set_xlabel("Movie Title")

    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Ratings for " + title)

    fig.tight_layout()

    plt.savefig("img/histogram_" + filename)
    plt.clf()

def makeScatterPlot(movies, filename, title):
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
    fig.savefig("img/scatter_" + filename)
    fig.clf()

def part1():
    makeHistogram(every, "all.png", "All Movies")
    makeHistogram(dramas, "drama.png", "Drama Movies")
    makeHistogram(horrors, "horror.png", "Horror Movies")
    makeHistogram(actions, "action.png", "Action Movies")
    makeHistogram(popular, "popular.png", "10 Most Popular Movies", aggregate=False)
    makeHistogram(best, "best.png", "10 Highest Rated Movies", aggregate=False)

def part2():
    makeScatterPlot(random, "random.png", "10 Random Movies")
    makeScatterPlot(popular, "popular.png", "10 Most Popular Movies")
    makeScatterPlot(best, "best.png", "10 Highest Rated Movies")
    makeScatterPlot(dramas[:10], "drama.png", "10 Drama Movies")
    makeScatterPlot(horrors[:10], "horror.png", "10 Horror Movies")
    makeScatterPlot(actions[:10], "action.png", "10 Action Movies")

def old():
    # I moved all the old code here
    labels = ['1', '2', '3', '4', '5']
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', '#cc99ff']
    explode = (0, 0, 0, 0, 0)
    plt.pie(n, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=180)
    plt.axis('equal')
    plt.title("Distribution of Ratings", y=1.025)
    plt.savefig('ratingsPie.png')
    plt.clf()

    numRatings = []
    for movie in popular:
        numRatings.append(movieInfo[movie]['ratings'])

    plt.hist(numRatings, bins=[1,2,3,4,5,6], align='left', stacked=True)
    plt.title("Distribution of Ratings for Most Popular Movies")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.savefig('popularFreq.png')
    plt.clf()

    print("BEST RATED")
    for movie in best:
        print(movieInfo[movie]['title'], np.mean(movieInfo[movie]['ratings']), len(movieInfo[movie]['ratings']))

part1()
part2()
