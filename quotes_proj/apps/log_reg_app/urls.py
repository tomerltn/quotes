from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^auth$', views.auth),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<users_id>\d+)$', views.user),
    url(r'^edit_user/(?P<users_id>\d+)$', views.edit_user),
   
]