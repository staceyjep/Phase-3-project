from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models.base import Base
from lib.models.movie import movie_actor

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

   
    movies = relationship("Movie", secondary=movie_actor, back_populates="actors")

    def __repr__(self):
        return f"<Actor name='{self.name}' age={self.age}>"
