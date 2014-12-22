from django.conf.urls import patterns, url

from eq import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^cart/(?P<employe_id>\d+)/', views.cart, name='cart'),
    url(r'^empl/', views.empl, name='empl'),
)