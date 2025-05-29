from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Movie, Director, Actor, Crew

engine = create_engine('sqlite:///films.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    Base.metadata.create_all(engine)

    # Example seed
    nolan = Director(name="Christopher Nolan", nationality="British-American")
    leo = Actor(name="Leonardo DiCaprio", age=49)
    hans = Crew(name="Hans Zimmer", role="Composer")
    inception = Movie(title="Inception", genre="Sci-Fi", director=nolan)

    inception.actors.append(leo)
    inception.crew_members.append(hans)

    session.add_all([nolan, leo, hans, inception])
    session.commit()
    print("🌱 Database seeded with Inception.")

if __name__ == "__main__":
    seed_data()
