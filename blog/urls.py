from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
   
    path("", views.blog_index, name="blog_index"),
    path("post/<slug>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('summernote/', include('django_summernote.urls')),
]