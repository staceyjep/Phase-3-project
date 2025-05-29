from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from lib.models.base import Base

# Association tables for many-to-many relationships
movie_actor = Table(
    'movie_actor', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)

movie_crew = Table(
    'movie_crew', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('crew_id', Integer, ForeignKey('crew.id'))
)

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    director_id = Column(Integer, ForeignKey('directors.id'))

    # Relationships
    director = relationship("Director", back_populates="movies")
    actors = relationship("Actor", secondary=movie_actor, back_populates="movies")
    crew_members = relationship("Crew", secondary=movie_crew, back_populates="movies")

    def __repr__(self):
        return f"<Movie title='{self.title}' genre='{self.genre}'>"
