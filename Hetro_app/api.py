from tastypie.serializers import Serializer
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest
from django.contrib.auth.models import User
from Hetro_app.models import *


class UserResource(ModelResource):
	class Meta:
		# For authentication, allow both basic and api key so that the key
		# can be grabbed, if needed.
		authentication = Authentication()
		authorization = Authorization()
		serializer = Serializer(formats=['json'])

		# Because this can be updated nested under the UserProfile, it needed
		# 'put'. No idea why, since patch is supposed to be able to handle
		# partial updates.
		allowed_methods = ['get', 'put' ]
		always_return_data = True
		queryset = User.objects.all()#.select_related("api_key")
		resource_name = "users"
		fields = ['last_name','first_name','username','is_active','email','is_staff','is_superuser']
		filtering = {'username':ALL_WITH_RELATIONS,'email':ALL}


class ProfileResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user', full=False)
	class Meta:
		# For authentication, allow both basic and api key so that the key
		# can be grabbed, if needed.
		authentication = Authentication()
		authorization = Authorization()
		serializer = Serializer(formats=['json'])

		# Because this can be updated nested under the UserProfile, it needed
		# 'put'. No idea why, since patch is supposed to be able to handle
		# partial updates.
		allowed_methods = ['get', 'put' ]
		always_return_data = True
		queryset = Profile.objects.all()#.select_related("api_key")
		resource_name = "profiles"


class ArtistResource(ModelResource):
	profile = fields.ForeignKey(ProfileResource, 'profile', full=False)
	albums = fields.ToManyField('Hetro_app.api.AlbumResource', 'albums', full=False)
	class Meta:
		# For authentication, allow both basic and api key so that the key
		# can be grabbed, if needed.
		authentication = Authentication()
		authorization = Authorization()
		serializer = Serializer(formats=['json'])

		# Because this can be updated nested under the UserProfile, it needed
		# 'put'. No idea why, since patch is supposed to be able to handle
		# partial updates.
		allowed_methods = ['get', 'put' ]
		always_return_data = True
		queryset = Artist.objects.all()#.select_related("api_key")
		resource_name = "artists"

class AlbumResource(ModelResource):
	class Meta:
		# For authentication, allow both basic and api key so that the key
		# can be grabbed, if needed.
		authentication = Authentication()
		authorization = Authorization()
		serializer = Serializer(formats=['json'])

		# Because this can be updated nested under the UserProfile, it needed
		# 'put'. No idea why, since patch is supposed to be able to handle
		# partial updates.
		allowed_methods = ['get', 'put' ]
		always_return_data = True
		queryset = Album.objects.all()#.select_related("api_key")
		resource_name = "albums"

class SongResource(ModelResource):
	class Meta:
		# For authentication, allow both basic and api key so that the key
		# can be grabbed, if needed.
		authentication = Authentication()
		authorization = Authorization()
		serializer = Serializer(formats=['json'])

		# Because this can be updated nested under the UserProfile, it needed
		# 'put'. No idea why, since patch is supposed to be able to handle
		# partial updates.
		allowed_methods = ['get', 'put' ]
		always_return_data = True
		queryset = Song.objects.all()#.select_related("api_key")
		resource_name = "songs"

class FeaturedSongsResource(ModelResource):
	class Meta:
		# For authentication, allow both basic and api key so that the key
		# can be grabbed, if needed.
		authentication = Authentication()
		authorization = Authorization()
		serializer = Serializer(formats=['json'])

		# Because this can be updated nested under the UserProfile, it needed
		# 'put'. No idea why, since patch is supposed to be able to handle
		# partial updates.
		allowed_methods = ['get', 'put' ]
		always_return_data = True
		queryset = FeaturedSongs.objects.all()#.select_related("api_key")
		resource_name = "featuredsongs"
