from Database.connection import get_connection
class ChiefCrew:
    def __init__(self,id,name,category):
        self.id=id
        self._name=name
        self._category=category
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        if not isinstance(id,int):
            raise TypeError('id must be an integer')
        self._id=id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if len(name)<2:
            raise ValueError('name must be at least 2 characters')
        self._name=name
    @property   
    def category(self):
        return self._category
    @category.setter
    def catgeory(self,category):
        categories=['camera','sound','lighting','editing','casting']
        if category not in categories:
            raise ValueError('category must be one of the following: camera,sound,lighting,editing,casting')
        self._category=category
    #get movies based on crew
    @property
    def movies(self):
        from lib.movies import Movie
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
            SELECT m.id,m.title,m.genre,m.director_id,m.chief_crew_id,m.actors_id
            FROM movies m
            JOIN chief_crew c ON m.chief_crew_id=c.id
            WHERE c.name=?
        ''',(self._name,))
        movies=cursor.fetchall()
        conn.close()
        if movies:
            return [Movie(movie['id'],movie['title'],movie['genre'],movie['director_id'],movie['chief_crew_id'],movie['actors_id']) for movie in movies]
        else:
            return []
    #final representation
    def __repr__(self):
        movie_names=', '.join([movie.title for movie in self.movies])
        return f'<Crew-Member {self.name}:Category:{self.category}| Movies: {movie_names}>'