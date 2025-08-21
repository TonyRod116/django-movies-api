from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializer import MovieSerializer

# Create your views here.
# Patch: /countries/
class MovieView(APIView):

    # Index route
    # Method: GET
    def get(self, request):
        movies = Movie.objects.all()
        serialized_movies = MovieSerializer(movies, many=True)
        return Response(serialized_movies.data)
    
    # Create route
    # Method: POST
    def post(self, request):
        return Response("HIT CREATE ROUTE")