from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="entry_page"),
    path("error_404", views.error_404_view, name="error_404"),
    path("search", views.search, name="search"),
    path("search_results/<str:search_query>", views.search_results, name="search_results"),
    path("new_page", views.new_page, name="new_page"),
    path("save_page", views.save_page, name="save_page"),
]


handler404 = 'encyclopedia.views.error_404_view'
