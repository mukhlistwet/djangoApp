
from django.contrib import admin
from django.urls import path, include
from . import views 


from blog import views as blog_view
from about import views as about_view


urlpatterns = [
    path('blog/', include('blog.urls')),
	path('', views.index), 
    path('home/', views.index), 
   	path('about/',about_view.index),
    #path('blog/', blog_view.index),

   
    path('admin/', admin.site.urls),

]
