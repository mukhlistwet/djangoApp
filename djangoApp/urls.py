
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views 


from blog import views as blog_view
from about import views as about_view


urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index),
    url(r'^home/$',views.index),
    url(r'^about/', include('about.urls')),
    #url(r'^about/$',about_view.index),
   	#path('about/',about_view.index),
    #path('blog/', blog_view.index),
    #path('home/', views.index),
   
    path('admin/', admin.site.urls),

]
