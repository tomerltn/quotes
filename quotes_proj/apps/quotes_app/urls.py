from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_quote$', views.add_quote),
    url(r'^view_poster/(?P<quotes_id>\d+)$', views.view_poster),
    url(r'^like_quote/(?P<quotes_id>\d+)$', views.like_quote),
    url(r'^delete_quote/(?P<quotes_id>\d+)$', views.delete_quote),
]