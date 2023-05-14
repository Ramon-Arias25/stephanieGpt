import omdb
from Stephanie.Modules.base_module import BaseModule


class MovieInformationModule(BaseModule):
    def __init__(self, *args):
        super(MovieInformationModule, self).__init__(*args)

    def give_some_information(self):
        self.assistant.say("¿de qué película te gustaría saber?")
        movie_name = self.assistant.listen().decipher()
        movies = omdb.search_movie(movie_name)
        if len(movies) > 0:
            movies.sort(key=lambda x: x.year, reverse=True)
            for i in range(0, len(movies)):
                if i == 0:
                    speech = "¿La película a la que te refieres es %s, estrenada en %s ?" % (
                        movies[i].title, movies[i].year)
                else:
                    speech = "Muy bien, entonces que tal %s, estrenada en %s ?" % (
                        movies[i].title, movies[i].year)
                self.assistant.say(speech)
                response = self.assistant.listen().decipher()
                if len(response.split()) > 3:
                    return "Hey, ¿Estás un poco de mal humor?."
                elif response == "si":
                    imdb_id = movies[i].imdb_id
                    print("found")
                    return self.give_movie_information_from_imdb_id(imdb_id)
        else:
            return "Lo siento, pero no te entiendo. Intentalo otra vez por favor"

    @staticmethod
    def give_movie_information_from_imdb_id(imdb_id):
        movie = omdb.imdbid(imdb_id)
        speech = "%s fue lanzado en %s, dirigido por %s del genero %s tiene un tiempo de ejecución de aproximadamente %s" \
                 "obtuvo una calificación de %s presentando %s tenía una trama como %s" % ( movie.title, 
                                                                                            movie.released,
                                                                                            movie.director, 
                                                                                            movie.genre,
                                                                                            movie.runtime, 
                                                                                            movie.imdb_rating,
                                                                                            movie.actors, 
                                                                                            movie.plot)
        return speech
