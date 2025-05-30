from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models.base import Base

class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nationality = Column(String)

    
    movies = relationship("Movie", back_populates="director")

    def __repr__(self):
        return f"<Director name='{self.name}' nationality='{self.nationality}'>"
