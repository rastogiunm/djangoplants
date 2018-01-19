from django.conf.urls import url, include
from . import views

from django.views.generic import ListView, DetailView
from plantapp.models import Plant

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/$', ListView.as_view(queryset=Plant.objects.all().order_by("-Name")[:25],
                                    template_name="plantapp/plantlist.html")),
    url(r'^edit/(?P<pk>\d+)$', DetailView.as_view(model=Plant,
                                    template_name="plantapp/plantdetail.html")),                                
    url(r'^contact/', views.contact, name='contact'),
]