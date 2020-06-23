from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name ='blog'

urlpatterns = [
    path('', views.all_blog, name= 'all_blog'),
    path('<int:blog_id>', views.content, name= 'blog_content'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)