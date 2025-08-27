from .common import MovieSerializer
from users.serializers.common import OwnerSerializer
from actors.serializers.common import ActorSerializer


class PopulatedMovieSerializer(MovieSerializer):
    owner = OwnerSerializer()
    actors = ActorSerializer(many=True)