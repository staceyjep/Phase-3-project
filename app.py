from Database.connection import get_connection
from Database.setup import create_tables
from lib.movies import Movie
from lib.actors import Actor
from lib.crew import ChiefCrew
from lib.directors import Director
#Remove data from all the tables.
def clear_data():
    while True:
        confirm = input("Are you sure you want to delete all data? (y/n): ").strip().lower()
        if confirm == "y":
            code="1234"
            confirm_code=input("Enter the code: ")
            if confirm_code==code:
                break
            else:
                print("Invalid code. Please try again.")
        elif confirm == "n":
            return
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('DELETE FROM movies')
    cursor.execute('DELETE FROM actors')
    cursor.execute('DELETE FROM directors')
    cursor.execute('DELETE FROM chief_crew')
    conn.commit()
    conn.close()
#Delete data from a specific table.
def delete_data():
    while True:
        delete_option = input("Enter what you want to delete (movie, director, crew, actor): ").strip().lower()
        if delete_option not in ["movie", "director", "crew", "actor"]:
            print("Invalid option. Please choose from 'movie', 'director', 'crew', or 'actor'.")
        else:
            break
    name_to_delete = input("Enter the name of the {}: ".format(delete_option))
    conn = get_connection()
    cursor = conn.cursor()
    
    if delete_option == "movie":
        cursor.execute("DELETE FROM movies WHERE title=?", (name_to_delete,))
    elif delete_option == "director":
        cursor.execute("DELETE FROM directors WHERE name=?", (name_to_delete,))
    elif delete_option == "crew":
        cursor.execute("DELETE FROM chief_crew WHERE name=?", (name_to_delete,))
    elif delete_option == "actor":
        cursor.execute("DELETE FROM actors WHERE name=?", (name_to_delete,))
    
    conn.commit()
    conn.close()
    print("Deleted {} '{}' successfully.".format(delete_option, name_to_delete))
#Add data to all the tables.
def main():
    create_tables()
    while True:
        movie_name=input("Enter Movie's name: ")
        if len(movie_name)<2:
            print("Movie name must be at least 2 characters")
        else:
            break
    while True:
        movie_genre=input("Enter Movie's genre(action,comedy,drama,horror,romance): ")
        genres=['action','comedy','drama','horror','romance']
        if movie_genre not in genres:
            print("Genre must be one of the following: action,comedy,drama,horror,romance")
        else:
            break
    while True:
        movie_director=input("Enter Movie's director: ")
        if len(movie_director)<2:
            print("Director name must be at least 2 characters")
        else:
            break
    while True:
        movie_chief_crew=input("Movie's crew member: ")
        if len(movie_chief_crew)<2:
            print("chief crew member name must be at least 2 characters")
        else:
            break
    while True:
        categories=['sound','visual','light','sound,visual','light,sound,visual','light,visual','sound,light,visual']
        movie_chief_crew_category=input(" chief crew member's category(sound,visual,light): ")
        if movie_chief_crew_category not in categories:
            print("chief crew member's category must be one of the following: sound,visual,light")
        else:
            break
    while True:
        movie_actors=input("Enter Movie's main actor: ")
        if len(movie_actors)<2:
            print("Actor name must be at least 2 characters")
        else:
            break
    
   
    conn=get_connection()
    cursor=conn.cursor()
    ##############################
    #actors
    cursor.execute('SELECT id FROM actors WHERE name=?',(movie_actors,))
    actor_info=cursor.fetchone()
    if actor_info:
        actor_id=actor_info[0]
    else:
        cursor.execute('INSERT INTO actors(name) VALUES(?)',(movie_actors,))
        actor_id=cursor.lastrowid
    #directors
    cursor.execute('SELECT id FROM directors WHERE name=?',(movie_director,))
    director_info=cursor.fetchone()
    if director_info:
        director_id=director_info[0]
    else:
        cursor.execute('INSERT INTO directors(name) VALUES(?)',(movie_director,))
        director_id=cursor.lastrowid
    #chief crew
    cursor.execute('SELECT id FROM chief_crew WHERE name=? AND category=?',(movie_chief_crew,movie_chief_crew_category))
    chief_crew_info=cursor.fetchone()
    if chief_crew_info:
        chief_crew_id=chief_crew_info[0]
    else:
        cursor.execute('INSERT INTO chief_crew(name,category) VALUES(?,?)',(movie_chief_crew,movie_chief_crew_category))
        chief_crew_id=cursor.lastrowid 
    #movies 
    cursor.execute("SELECT id FROM movies WHERE title=? AND director_id=?", (movie_name, director_id))
    existing_movie = cursor.fetchone()
    if existing_movie:
        movie_id = existing_movie[0]
        cursor.execute("UPDATE movies SET genre=?, chief_crew_id=?, actors_id=? WHERE id=?", (movie_genre, chief_crew_id, actor_id, movie_id))
    else:
        cursor.execute("INSERT INTO movies(title, genre, director_id, chief_crew_id, actors_id) VALUES(?, ?, ?, ?, ?)",
                       (movie_name, movie_genre, director_id, chief_crew_id, actor_id))
        movie_id = cursor.lastrowid
    #################################
    conn.commit()
    conn.close()
#list data in the database
def list_data():   
    while True:
        list_option = input("Enter what you want to list (all, movies, actors, directors, crew): ").strip().lower()
        if list_option not in ["all", "movies", "actors", "directors", "crew"]:
            print("Invalid option. Please try again.")
        else:
            break
    
    conn = get_connection()
    cursor = conn.cursor()

    if list_option == "all" or list_option == "movies":
        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()
        print("\nMovies:")
        for movie in movies:
            print(Movie(movie["id"], movie["title"], movie["genre"], movie["director_id"], movie["chief_crew_id"], movie["actors_id"]))
    
    if list_option == "all" or list_option == "actors":
        cursor.execute('SELECT * FROM actors')
        actors = cursor.fetchall()
        print("\nActors:")
        for actor in actors:
            print(Actor(actor["id"], actor["name"]))
    
    if list_option == "all" or list_option == "directors":
        cursor.execute('SELECT * FROM directors')
        directors = cursor.fetchall()
        print("\nDirectors:")
        for director in directors:
            print(Director(director["id"], director["name"]))
    
    if list_option == "all" or list_option == "crew":
        cursor.execute('SELECT * FROM chief_crew')
        chief_crew = cursor.fetchall()
        print("\nChief Crew:")
        for chief in chief_crew:
            print(ChiefCrew(chief["id"], chief["name"], chief["category"]))

    conn.close()

if __name__=="__main__":
    while True:
        command=input("Enter command(clear;Add;exit,Delete;List): ")
        if command.strip().lower()=="clear":
            clear_data()
        elif command.strip().lower()=="add":
            main()
        elif command.strip().lower()=="exit":
            exit()
        elif command.strip().lower()=="delete":
            delete_data()
        elif command.strip().lower()=="list":
            list_data()
        else:
            print("Invalid command, please try again")