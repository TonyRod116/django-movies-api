from django.urls import path
from .views import SignupView, SignInView


#already prefixed with '/users/'
urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', SignInView.as_view()),
]