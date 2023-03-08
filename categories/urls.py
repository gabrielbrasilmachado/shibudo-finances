from django.urls import path
from .views import CategoryView, CategoryDetailView

urlpatterns = [
    path("categories/", CategoryView.as_view()),
    path("categories/<category_id>", CategoryDetailView.as_view()),
]
