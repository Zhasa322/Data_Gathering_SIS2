import json
import re




#Load the file in read mode
with open("data/movies.json", "r") as f:
    movies = json.load(f)

#Remove duplicates using dictionary and then convert it back to the list, because there are no duplicates in dict
unique = {}
for movie in movies:
    movie_id = movie.get("imdb_id")
    unique[movie_id] = movie
movies = list(unique.values())

#Array for cleaned novies 
cleaned = []

#Clean the movie
for movie in movies:
    clean_movie = {}

    #ID
    clean_movie["id"] = int(re.sub("\\D", "", movie.get("imdb_id")))

    #Title we normalize it by making every word start with capital letter and remowing whitespaces
    clean_movie["title"] = movie.get("title").title().strip()

    #Rating
    clean_movie["rating"] = float(re.sub("\\D", "", movie.get("rating")))
    
    #Year
    clean_movie["year"] = int(re.sub("\\D", "", movie.get("year")))
    
    #Add movie to the movie list
    cleaned.append(clean_movie)




#Save to json in write mode
with open("data/cleaned_movies.json", "w") as f:
    json.dump(cleaned, f)