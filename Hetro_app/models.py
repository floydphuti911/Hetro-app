from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.

class Profile(models.Model):
	"""docstring for Profile"""
	user = models.OneToOneField(User, related_name='user_profile')
	
	def __unicode__(self):
		return self.user.username

		
class Artist(models.Model):
	"""docstring for Profile"""
	profile = models.ForeignKey(Profile, related_name='artist_profile')
	name = models.CharField(default='artist name',max_length=50)
	bio = models.CharField(default="Artist Biography",blank=True,max_length=500)
	genre = models.CharField(default="Various",blank=True,max_length=50)
	avatar = models.ImageField(null=True,blank=True,upload_to='artist_avatars')
	albums = models.ManyToManyField('Album',blank=True, related_name='artist_album')
	songs = models.ManyToManyField('Song',blank=True, related_name='artist_songs')
	genre = models.CharField(max_length=100, blank=True, default="Various")
	slug = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return self.name

	def get_unique_slug(self):
		slug = slugify(self.name)
		unique_slug = slug
		num = 1
		while Artist.objects.filter(slug=unique_slug).exists():
			if Artist.objects.get(slug=unique_slug).pk != self.pk:
				unique_slug = '{}-{}'.format(slug, num)
				num += 1
			else:
				return unique_slug
		return unique_slug
 
	def save(self, *args, **kwargs):
		self.slug = self.get_unique_slug()
		super(Artist, self).save()		
		
class Album(models.Model):
	name = models.CharField(default='album_name',max_length=50)
	art = models.ImageField(null=True,blank=True,upload_to='album_art', default='album_art/default-album.png')
	songs = models.ManyToManyField('Song',blank=True, related_name='album_songs')
	published = models.BooleanField(default=False)
	release_date = models.DateTimeField()
	slug = models.CharField(max_length=100, blank=True)
	trending = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

	def get_unique_slug(self):
		slug = slugify(self.name)
		unique_slug = slug
		num = 1
		while Album.objects.filter(slug=unique_slug).exists():
			if Album.objects.get(slug=unique_slug).pk != self.pk:
				unique_slug = '{}-{}'.format(slug, num)
				num += 1
			else:
				return unique_slug
		return unique_slug
 
	def save(self, *args, **kwargs):
		self.slug = self.get_unique_slug()
		super(Album, self).save()		

			
class Song(models.Model):
	title = models.CharField(null=True,blank=True,max_length=50)
	track = models.FileField(null=True,blank=True,upload_to='tracks')
	genre = models.CharField(default="Various",blank=True,max_length=50)
	Realease_date = models.DateTimeField()
	published = models.BooleanField(default=False)
	slug = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return self.title if self.title else str(self.id)

	def get_unique_slug(self):
		slug = slugify(self.title)
		unique_slug = slug
		num = 1
		while Song.objects.filter(slug=unique_slug).exists():
			if Song.objects.get(slug=unique_slug).pk != self.pk:
				unique_slug = '{}-{}'.format(slug, num)
				num += 1
			else:
				return unique_slug
		return unique_slug
 
	def save(self, *args, **kwargs):
		self.slug = self.get_unique_slug()
		super(Song, self).save()				


class FeaturedSongs(models.Model):

	featured = models.ManyToManyField(Song,related_name='feature_songs')

	def __unicode__(self):
		return self.published
		
def signals_import():
    """ A note on signals.
    The signals need to be imported early on so that they get registered
    by the application. Putting the signals here makes sure of this since
    the models package gets imported on the application startup.
    """
    from tastypie.models import create_api_key
    
    models.signals.post_save.connect(create_api_key, sender=User)
   

signals_import()
	

      

   	





		