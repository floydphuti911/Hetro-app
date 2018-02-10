"""Hetro_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
#from django.conf.urls.static import static
from django.views import static
from Hetro_app.views import *
from Hetro_app.api import *
from tastypie.api import Api
from django.conf.urls import  include, url

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ProfileResource())
v1_api.register(ArtistResource())
v1_api.register(AlbumResource())
v1_api.register(SongResource())
v1_api.register(FeaturedSongsResource())

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^artist/(?P<slug>.*)$', ArtistView.as_view(), name="artist"),
url(r'^album/(?P<slug>.*)$', AlbumView.as_view(), name="album"),
url(r'^api/', include(v1_api.urls)),
url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),
url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
url(r'^$', HomeView.as_view(), name="homepage"),
]
