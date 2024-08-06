from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from .models import Artist, Album
from discos.forms import ArtistForm, AlbumForm

# Create your views here.

def index(request):
    albums = Artist.objects.order_by('name_album')
    context = {
        'albums': albums
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def artista(request, artist_id):
    artista = get_object_or_404(Artist, pk = artist_id)
    template = loader.get_template('display_artist.html')
    context = {
        'artista': artista
    }
    return HttpResponse(template.render(context, request))

def album(request, trainer_id):
    album = get_object_or_404(Album, pk = trainer_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

def list_album(request):
    albumes = Album.objects.order_by('name_album')
    context = {
        'albumes': albumes
    }
    template = loader.get_template('list_album.html')
    return HttpResponse(template.render(context, request))


def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = ArtistForm()
    
    return render(request, 'artist_form.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discos:list_trainer')
    else:
        form = AlbumForm()

    return render(request, 'album_form.html', {'form': form})


def edit_artists(request, id):
    pokemom = get_object_or_404(Artist, pk = id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = ArtistForm(instance=artista)
        
    return render(request, 'artist_form.html', {'form': form})

def edit_album(request, id):
    trainer = get_object_or_404(Album, pk = id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('discos:list_trainer')
    else:
        form = AlbumForm(instance=trainer)
    
    return render(request, 'album_form.html', {'form': form})


def delete_artist(request, id):
    artistas = get_object_or_404(Artist, pk = id)
    artistas.delete()
    return redirect("discos:index")
    

def delete_album(request, id):
    disco = get_object_or_404(Album, pk = id)
    disco.delete()
    return redirect('discos:list_album')

    
    
    
    