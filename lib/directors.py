from Database.connection import get_connection
class Director:
    def __init__(self,id,name):
        self._id=id
        self._name=name
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
    #get movies based on director
    @property
    def movies(self):
        from lib.movies import Movie
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
            SELECT m.id, m.title,m.genre,m.director_id,m.chief_crew_id,m.actors_id
            FROM movies m
            JOIN directors d ON m.director_id=d.id
            WHERE d.name=?
            ''',(self._name,))
        movies=cursor.fetchall()
        conn.close()
        if movies:
            return [Movie(movie['id'],movie['title'],movie['genre'],movie['director_id'],movie['chief_crew_id'],movie['actors_id']) for movie in movies]
        else:
            return []
    #get actors based on director
    @property
    def actors(self):
        from lib.actors import Actor
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
            SELECT a.id,a.name
            FROM actors a
            JOIN movies m ON a.id=m.actors_id
            JOIN directors d ON m.director_id=d.id
            WHERE d.name=?
            ''',(self._name,))
        actors=cursor.fetchall()
        conn.close()
        if actors:
            return [Actor(actor['id'],actor['name']) for actor in actors]
        else:
            return []
    #final representation
    def __repr__(self):
        actor_names=', '.join([actor.name for actor in self.actors])
        movie_names=', '.join([movie.title for movie in self.movies])
        return f'<Director {self.name} | Movies: {movie_names} | Actors: {actor_names}>'