def add_movie(database,name,director,year,runtime):
    entry = {"name":name,"director":director,"year":year,"runtime":runtime}

    database.append(entry)

def find_movies(database: list, search_term: str):
    movies = []
    find = str.upper(search_term)

    for i in database:
        if find in str.upper(i["name"]):
            movies.append(i)

    return movies
if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    add_movie(database,"Programming", "Vicente Ramos", 1998,25)
    print(database)

    mymovies = find_movies(database,"python")
    print(mymovies)