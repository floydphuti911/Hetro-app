from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from Hetro_app.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

 
class HomeView(View):
	def get(self,request, *args, **kwargs):
		context = {}
		artists = Artist.objects.filter()
		paginator = Paginator(artists, 3) # Show 25 contacts per page
		page = request.GET.get('page')
		try:
			artists = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			artists = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			artists = paginator.page(paginator.num_pages)

		context['artists'] = artists
		return render(request,'home.html', context) 


class ArtistView(View):
	def get(self,request, *args, **kwargs):
		artist = get_object_or_404(Artist,slug=kwargs.get('slug'))
		context = {'artist': artist}

		albums = artist.albums.all()
		paginator = Paginator(albums, 3) # Show 3 contacts per page
		page = request.GET.get('albums')
		try:
			albums = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			albums = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			albums = paginator.page(paginator.num_pages)

		context['albums'] = albums

		songs = artist.songs.filter()
		paginator = Paginator(albums, 25) # Show 25 contacts per page
		page = request.GET.get('songs')
		try:
			songs = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			songs = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			songs = paginator.page(paginator.num_pages)

		context['songs'] = songs

		return render(request,'artist.html',context) 
