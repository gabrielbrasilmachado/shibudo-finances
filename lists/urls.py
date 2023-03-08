from django.urls import path
from .views import ListView, ListDetailView
from finances.views import FinanceView, FinanceDetailView

urlpatterns = [
    path("lists/", ListView.as_view()),
    path("lists/<list_id>/", ListDetailView.as_view()),
    path("lists/<list_id>/finances/", FinanceView.as_view()),
    path("lists/<list_id>/finances/<finance_id>/", FinanceDetailView.as_view()),
]
