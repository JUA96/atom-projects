# 1) Load the provided list of movies dictionaries.
# So we start with a list of dictionaries. Remember:
# lists are ordered so movies[0] will always return the first and movies[-1] will return the last. If it has an order then it also means we can sort it too. dictionaries are unordered, they just take a key movies[0]['name']

# List of movies dictionaries:

movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


# 2) Filtering data by IMDb score:

# Function takes a single argument
# We expect that the movie has a key called `imdb`
# Just check it's greater than 5.5
def movie_is_decent(movie):
    return movie['imdb'] > 5.5

# Iterate over all the movies and check whether each one is any good. Then I'll print a string depending on the answer.


for movie in movies:
    if movie_is_decent(movie):
        print(movie['name'], 'is decent')
    else:
        print(movie['name'], 'is total crap')

# A list comprehension (my fave)
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions


def category_score_1(movies, category_name):
    # Create a new list by filtering the movies
    movies_in_category = [
        movie for movie in movies if movie['category'] == category_name
    ]

    # Create a new list just containing the scores
    scores = [movie['imdb'] for movie in movies_in_category]

    # Compute the average
    average_score = sum(scores) / len(scores)
    return average_score


category_score_1(movies, 'Romance')

# Append in a for loop


def category_score_2(movies, category_name):
    # Create a new list by filtering the movies
    movies_in_category = []
    for movie in movies:
        if movie['category'] == category_name:
            movies_in_category.append(movie)
    # Create a new list just containing the scores
    scores = []
    for movie in movies_in_category:
        scores.append(movie['imdb'])

    # Compute the average
    average_score = sum(scores) / len(scores)
    return average_score


category_score_2(movies, 'Romance')

# Write a function that:

# Accepts the list of movies and a specified IMDb score. 2) Returns the sublist of movies that have scores greater than the one specified.


def filter_on_score(movies, score):
    return [movie for movie in movies if movie['imdb'] > score]

# OR


def filter_on_score(movies, score):
    movies_filtered = []
    for movie in movies:
        if movie['imdb'] > score:
            movies_filtered.append(movie)
    return movies_filtered


filter_on_score(movies, 7)

# Write a function that accepts the movies list sorted first by category and then by movie according to category average score and individual IMDb score, respectivley.


def ranked_movies_1(movies):
    # Add a new entry to each movie that is the category score we computed earlier
    for movie in movies:
        movie['category_score'] = category_score_1(movies, movie['category'])

    # Sort the movies. We'll use the built in sort operation, which can take two keys
    return sorted(movies, key=lambda movie: (movie['category_score'], movie['imdb']))


ranked_movies_1(movies)


def ranked_movies_2(movies):
    # Get the unique categories (this is how we reduce the computation)
    # I use a list comprehension to create a new list with all the categories
    # Then we turn it into a set (which only keeps the unique values)
    categories = set([movie['category'] for movie in movies])

    # WHOA!!! We can do dict-comprehensions too!
    # This is our lookup table. So the key is the category name
    # and the value is the category score.
    # Note we're only computing the score once per category - we got our optimisation
    category_scores = {
        category_name: category_score_1(movies, category_name)
        for category_name in categories
    }

    # Now we enrich the records
    for movie in movies:
        movie['category_score'] = category_scores[movie['category']]

    return sorted(movies, key=lambda movie: (movie['category_score'], movie['imdb']))


ranked_movies_2(movies)
