from lib.models import Movie, Director, Actor, Crew

def add_entry(session):
    print("\nWhat would you like to add?")
    print("1. Movie")
    print("2. Director")
    print("3. Actor")
    print("4. Crew Member")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        title = input("Movie title: ")
        genre = input("Genre: ")
        director_name = input("Director name: ")

        # Reuse existing director or create a new one
        director = session.query(Director).filter_by(name=director_name).first()
        if not director:
            director = Director(name=director_name)
        
        movie = Movie(title=title, genre=genre, director=director)
        session.add(movie)
        session.commit()
        print(f" Added movie: {title}")

    elif choice == "2":
        name = input("Director's name: ")
        nationality = input("Nationality: ")
        session.add(Director(name=name, nationality=nationality))
        session.commit()
        print(f"Added director: {name}")

    elif choice == "3":
        name = input("Actor's name: ")
        age = input("Age: ")
        session.add(Actor(name=name, age=int(age)))
        session.commit()
        print(f"Added actor: {name}")

    elif choice == "4":
        name = input("Crew member's name: ")
        role = input("Their role (e.g., editor, composer): ")
        session.add(Crew(name=name, role=role))
        session.commit()
        print(f"Added crew member: {name}")

    else:
        print(" Invalid choice.")

def list_all_entries(session):
    print("\n All Movies:")
    for movie in session.query(Movie).all():
        print(f" - {movie.title} ({movie.genre})")

    print("\n🎬 Directors:")
    for director in session.query(Director).all():
        print(f" - {director.name} [{director.nationality}]")

    print("\n🎭 Actors:")
    for actor in session.query(Actor).all():
        print(f" - {actor.name}, Age: {actor.age}")

    print("\n🎧 Crew Members:")
    for crew in session.query(Crew).all():
        print(f" - {crew.name} — {crew.role}")

def delete_entry(session):
    print("\nDelete from:")
    print("1. Movie")
    print("2. Director")
    print("3. Actor")
    print("4. Crew")

    choice = input("Choose category (1-4): ")
    name = input("Enter name/title to delete: ").strip()

    model_map = {
        "1": Movie,
        "2": Director,
        "3": Actor,
        "4": Crew
    }

    model = model_map.get(choice)

    if model:
        item = session.query(model).filter_by(name=name).first()
        if item:
            session.delete(item)
            session.commit()
            print(" Deleted successfully.")
        else:
            print(" Not found.")
    else:
        print(" Invalid category.")

def clear_database(session):
    session.query(Movie).delete()
    session.query(Director).delete()
    session.query(Actor).delete()
    session.query(Crew).delete()
    session.commit()
    print(" Database cleared.")
