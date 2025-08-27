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

class LanguageDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]