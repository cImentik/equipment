from django.conf.urls import patterns, url

from eq import views

urlpatterns = patterns('',
    url(r'^$', views.master, name='master'),
    url(r'^cart/(?P<employe_id>\d+)/', views.cart, name='cart'),
    url(r'^expends/', views.expend_list, name='expend_list'),
    url(r'^expend/', views.expend, name='expend'),
    url(r'^instock/', views.instock_list, name='instock_list'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.login, name='logout'),
    #url(r'^main/', views.main, name='main'),
    url(r'^safetyeng/', views.safetyeng, name='safetyeng'),
    url(r'^stock/', views.stock, name='stock'),
    url(r'^addempl/', views.addempl, name='addempl'),
    url(r'^delempl/', views.delempl, name='delempl'),
    url(r'^editempl/', views.editempl, name='editempl'),
    url(r'^cartprint/(?P<employe_id>\d+)/', views.cartprint, name='cartprint'),
    url(r'^balance/', views.balance, name='balance'),
    url(r'^addeq/', views.addeq, name='addeq'),
    url(r'^staff/', views.staff, name='staff'),
    url(r'^addunit/', views.addunit, name='addunit'),
)