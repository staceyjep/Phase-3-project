from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models.base import Base
from lib.models.movie import movie_crew

class Crew(Base):
    __tablename__ = 'crew'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)

    movies = relationship("Movie", secondary=movie_crew, back_populates="crew_members")

    def __repr__(self):
        return f"<Crew name='{self.name}' role='{self.role}'>"
