from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Actor
from .serializers.common import ActorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.

class ActorListCreateView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ActorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return ActorSerializer