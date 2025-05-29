from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Movie, Director

engine = create_engine('sqlite:///films.db')
Session = sessionmaker(bind=engine)
session = Session()

def debug():
    print("\n🔍 Debugging Movie List:")
    movies = session.query(Movie).all()
    for movie in movies:
        print(f"{movie.title} by {movie.director.name}")

if __name__ == "__main__":
    debug()
