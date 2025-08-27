from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers.common import MovieSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
# Patch: /countries/
class MovieView(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Index route
    # Method: GET
    def get(self, request):
        movies = Movie.objects.all()
        serialized_movies = MovieSerializer(movies, many=True)
        return Response(serialized_movies.data)
    
    # Create route
    # Method: POST
    def post(self, request):
        serialized_movies = MovieSerializer(data=request.data)

        # is_valid does the following: 
        # 1. takes the request.data and tries to vlaidate it based on the model
        # 2. if it fails it returns false, also adds an error key onto the serialized_movies object
        # 3. if it succeeds it returns true, also adds the data key onto the serialized_movies object
        # 4. if we set the raise_exception to true, it will raise Rest Framework's own ValidationError exception
        # ? Remember, all Rest Framework exceptions are  automatically handled by APIView, sending the relevant response

        serialized_movies.is_valid(raise_exception=True)

        # if validations succeeds, we can save the data
        serialized_movies.save(owner=request.user)

        # if validations fails, we can access the errors
        # print(serialized_movies.errors)

        return Response(serialized_movies.data, status=201)




# Path: /countries/<int:pk>
class MovieDetailView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    #helper function that attempts to get the specified object, but sends a 404 if not found
    # 1. get_movie will take the PK from the URL params as an argument
    # 2. it will attempt to get the object from the database
    # 3. if it succeeds, it will return the object
    # 4. if it fails, it will raise a DoesNotExist exception then he will send a 404 by raising NotFound
    def get_movie(self,pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist as e:
            raise NotFound("Movie does not exist")


    # Show route
    # Method: GET
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk) # Country.findOne({ _id: req.params.countryId})
        serialized_movie = MovieSerializer(movie)
        return Response(serialized_movie.data)


    # Update route
    # Method: PUT
    def put(self, request, pk):
        movie = self.get_movie(pk)

        # after retrieving country from database, deny acces if the logged in user s not the owner
        if movie.owner != request.user:
            raise PermissionDenied("Unauthorized: You do not have permission to access this resource") #raising a PermissionDenied exception will automatically send a 403 Forbidden response

        # if the user is the owner, continue
        serialized_movie = MovieSerializer(movie, data=request.data)
        serialized_movie.is_valid(raise_exception=True)
        serialized_movie.save(owner=request.user)
        return Response(serialized_movie.data)  



    # Delete route
    # Method: DELETE
    def delete(self, request, pk):
        movie = self.get_movie(pk)
        
        if movie.owner != request.user:
            raise PermissionDenied("Unauthorized: You do not have permission to access this resource")

        movie.delete()
        return Response(status=204)