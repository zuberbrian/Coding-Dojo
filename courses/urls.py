from django.conf.urls import url
from . import views
urlpatterns = [
   	url(r'^$', views.index),
	url(r'^process$', views.process),
	url(r'^destroy/(?P<number>\d+)$', views.destroy),
	url(r'^destroy/(?P<number>\d+)/confirm$', views.confirm),
]
