# Ingresar tus URLs de la app aquí
from django.urls import path

from . import views

app_name = "discos"
urlpatterns = [
    path("", views.index, name="index"),
    path("artist/<int:artist_id>/", views.artista, name="artist"),
    path("add_artist/", views.add_artist, name="add_artist"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("artist/edit/<int:id>/", views.edit_artist, name="edit_artist"),
    path("artist/delete/<int:id>/", views.delete_artist, name="delete_artist"),
    path("album/album/<int:album_id>/", views.album, name="album"),
    path("album/add_album/", views.add_album, name="add_album"),
    path("album/edit_album/<int:id>/", views.edit_album, name="edit_album"),
    path("album/delete_album/<int:id>/", views.delete_album, name="delete_album"),
    path("album/", views.list_album, name="list_album"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]
