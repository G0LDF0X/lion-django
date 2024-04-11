from django.shortcuts import render
from .models import Album, Photo
# Create your views here.
from django.views.generic import ListView, DetailView

class AlbumLV(ListView):
    model = Album
    template_name = "photo/object_list.html"

class AlbumDV(DetailView):
    model = Album
    template_name = "photo/album_detail.html"

class PhotoDV(DetailView):
    model = Photo
    template_name = "photo/photo_detail.html"