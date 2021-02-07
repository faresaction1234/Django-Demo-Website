from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.indexpage, name='indexpage'),
    url(r'^Aboutus/$', views.about_us, name='about_us'),
    url(r'^Contactus/$', views.contact_us, name='contact_us'),

]