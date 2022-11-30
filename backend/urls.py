from django.urls import path
from .views import UserView, UsersView

urlpatterns = [
    path('user', UserView.as_view()),
    path('users', UsersView.as_view()),

]