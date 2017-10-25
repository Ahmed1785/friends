from django.conf.urls import url
from . import views    

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^add/(?P<id>\d+)$', views.addFriend),
    url(r'^show/(?P<id>\d+)$', views.showUser), 
    url(r'^delete/(?P<id>\d+)$', views.deletePet),
    url(r'^home$', views.home),
]