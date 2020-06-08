from django.contrib import admin
from django.urls import path
import blog.views as blog_views




urlpatterns = [
    path('', blog_views.post_list_view, name='list'),
    path('<int:pk>', blog_views.post_detail_view, name='detail'),
]
