from django.contrib import admin
from django.urls import path
import blog.views as blog_views




urlpatterns = [
    path('', blog_views.post_list_view, name='list'),
    path('tag/<slug:tag_slug>', blog_views.post_list_view, name='tag_post_list'),
    path('<int:pk>', blog_views.post_detail_view, name='detail'),
]
