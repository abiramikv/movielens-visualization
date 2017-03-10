import matplotlib.pyplot as plt
import numpy as np
import pickle

with open('movie_info.pickle', 'rb') as handle:
    movieInfo = pickle.load(handle)

print movieInfo[0]

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
