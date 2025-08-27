from .common import ActorSerializer
from movies.serializers.populated import PopulatedMovieSerializer

class PopulatedActorSerializer(ActorSerializer):
    actors_movies = PopulatedMovieSerializer(many=True)
    