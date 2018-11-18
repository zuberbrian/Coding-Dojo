from django.conf.urls import url
from . import views

urlpatterns = [
   	url(r'^$', views.index),
	url(r'^new$', views.new),
	url(r'^users$', views.users),
	url(r'^(?P<number>\d)$', views.show),
	url(r'^(?P<number>\d)/edit$', views.edit),
	url(r'^create$', views.create),
	url(r'^(?P<number>\d)/destroy$', views.destroy),
]
