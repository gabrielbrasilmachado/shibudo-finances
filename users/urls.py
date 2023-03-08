from django.urls import path
from .views import UserCreateView, UserListView, UserDetailView
from rest_framework_simplejwt import views

urlpatterns = [
    path("users/", UserCreateView.as_view()),
    path("users/list/", UserListView.as_view()),
    path("login/", views.TokenObtainPairView.as_view()),
    path("refresh/", views.TokenRefreshView.as_view()),
    path("users/<user_id>/", UserDetailView.as_view()),
]
