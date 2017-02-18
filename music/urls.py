from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    #url(r'^$', views.index, name='index'),

    #/music/id/
    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
# With generic views
	#/music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]
