from django import forms 
from .models import Artist, Album

class AlbumForm(forms.ModelForm):
    class Meta: 
        model = Album
        fields = '__all__'
        widgets = {
            'name_album':forms.TextInput(attrs={'class': 'form-control'}),
            'release_year':forms.NumberInput(attrs={'class': 'form-control'}),
            'genre':forms.TextInput(attrs={'class': 'form-control'}),
            'artist_featuring':forms.Select(attrs={'class': 'form-control-file'}),
            'picture':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'name_artist':forms.TextInput(attrs={'class': 'form-control'}),
            'origin_country':forms.TextInput(attrs={'class': 'form-control'}),           
        }