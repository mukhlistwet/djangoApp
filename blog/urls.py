from django.urls import path

from . import views

urlpatterns = [
	url(r'^about/$',views.index),
	path('blog/',views.index),
]