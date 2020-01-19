movies = []

def menu():
    user_input= input(" enter 'a' add movie, 'l' show movie , 'f' find movie , 'q' exit ")


    while user_input != 'q':
        if user_input=='a':
            add_movies()
        elif user_input=='l':
            show_movies(movies)
        elif user_input=='f':
            find_movie()
        else:
            print('unknow  try again')

        user_input = input("\n enter 'a' add movie, 'l' show movie , 'f' find movie , 'q' exit ")




def add_movies():
    name =input('enter the movie')
    director= input('enter the name of director')
    year=input('enter year')

    movies.append({
        'name': name,
        'director': director,
        'year':year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")

def find_movie():
    find_by=input('what property')
    looking_for=input('search for')

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []
    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found


menu()





