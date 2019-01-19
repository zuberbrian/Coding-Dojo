from django.conf.urls import url
from . import views
urlpatterns = [
   	url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^signin$', views.signin),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^addjob$', views.addjob),
    url(r'^process$', views.process_new_job),
    url(r'^add/(?P<job_id>\d+)$', views.add_job_to_list),
    url(r'^view/(?P<job_id>\d+)$', views.job_detail),
    url(r'^remove/(?P<job_id>\d+)$', views.remove_job_from_list),
    url(r'^edit/(?P<job_id>\d+)$', views.edit),
    url(r'^delete/(?P<job_id>\d+)$', views.delete)
]
