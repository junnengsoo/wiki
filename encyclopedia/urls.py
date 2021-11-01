from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry_page, name="entry_page"),
    path("error_404", views.error_404_view, name="error_404")
]


handler404 = 'encyclopedia.views.error_404_view'
