from Database.connection import get_connection
class Movie:
    def __init__(self,id,title,genre,director_id,chief_crew_id,actors_id):
        self._id=id
        self._title=title
        self.genre=genre
        self.director_id=director_id
        self.chief_crew_id=chief_crew_id
        self.actors_id=actors_id
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        if not isinstance(id,int):
            raise TypeError('id must be an integer')
        self._id=id
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if len(title)<2:
            raise ValueError('title must be at least 2 characters')
        self._title=title
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self,genre):
        
        self._genre=genre
    #getting director based on movie
    @property
    def director(self):
        from lib.directors import Director
        director_info=self.get_director_info(self.director_id)
        if director_info:
            return Director(director_info['id'],director_info['name'])
        else:return None
   #getting actors based on movie
    @property
    def actors(self):
        from lib.actors import Actor
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
            SELECT a.id,a.name
            FROM actors a
            JOIN movies m ON a.id=m.actors_id
            WHERE m.id=?
        ''',(self.id,))
        actors=cursor.fetchall()
        conn.close()
        if actors:
            return [Actor(actor['id'],actor['name']) for actor in actors]
        else:
            return []
    #getting chief crew based on movie
    @property
    def chief_crew(self):
        from lib.crew import ChiefCrew
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
            SELECT c.id,c.name,c.category
            FROM chief_crew c
            JOIN movies m ON c.id=m.chief_crew_id
            WHERE m.id=?
        ''',(self._id,))
        chief_crew=cursor.fetchall()
        conn.close()
        if chief_crew:
            return [ChiefCrew(chief['id'],chief['name'],chief['category']) for chief in chief_crew]
        else:
            return []   
    #getting director info based on movie
    @staticmethod
    def get_director_info(director_id):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
            SELECT id,name
            FROM directors
            WHERE id=?
        ''',(director_id,))
        director_info=cursor.fetchone()
        conn.close()
        return director_info
    #final representation
    def __repr__(self):
        actor_names=', '.join([actor.name for actor in self.actors])
        director_names=self.director.name if self.director else 'Unknown'
        chief_crew_names=', '.join([chief_crew.name for chief_crew in self.chief_crew])
        chief_crew_category=', '.join([chief_crew.category for chief_crew in self.chief_crew])
        return f'<Movie:{self.title} | Director:{director_names} | Chief Crew:{chief_crew_names}:{chief_crew_category} | Actors:{actor_names}>'  