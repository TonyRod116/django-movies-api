from django.urls import path
from .views import ActorListCreateView, LanguageDetailView

urlpatterns = [
    path('', ActorListCreateView.as_view(), name='actor-list-create'),
    path('<int:pk>/', LanguageDetailView.as_view(), name='language-detail'),
]