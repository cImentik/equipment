from django.conf.urls import patterns, url

from eq import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^cart/(?P<employe_id>\d+)/', views.cart, name='cart'),
    url(r'^expends/', views.expend_list, name='expend_list'),
    url(r'^expend/', views.expend, name='expend'),
    url(r'^instock/', views.instock_list, name='instock_list'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.login, name='logout'),
)