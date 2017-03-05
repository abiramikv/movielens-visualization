import numpy as np

# dictionary of movies ids, containing containing {title, year, categories}
data = np.loadtxt("movies.txt", delimiter='\t', dtype=bytes)
data = [[item.decode() for item in row] for row in data]

label = data[56]

categories = ["Unknown", "Action", "Adventure", "Animation", "Childrens", "Comedy", "Crime", "Documentary",
"Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]

movies = []
movie = {'title':'', 'year':0, 'genre':[]}
genres = label[-19:]

for i, genre in enumerate(genres):
    if genre == "1":
        movie['genre'].append(categories[i])

print(label)



# for label in data:

    # movies.append(movie)
