from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
	#url(r'^about/$',views.index),
	url(r'^$',views.index),
	url(r'^news/$',views.news),
	url(r'^cerita/$',views.cerita),
	#url(r'^recent/$',views.index),
]