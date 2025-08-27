from django.urls import path
from .views import ActorListCreateView, ActorDetailView

urlpatterns = [
    path('', ActorListCreateView.as_view(), name='actor-list-create'),
    path('<int:pk>/', ActorDetailView.as_view(), name='actor-detail'),
]