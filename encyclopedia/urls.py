from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="entry_page"),
    path("error_404", views.error_404_view, name="error_404"),
    path("search", views.search, name="search"),
    path("search_results", views.search_results, name="search_results")
]


handler404 = 'encyclopedia.views.error_404_view'
