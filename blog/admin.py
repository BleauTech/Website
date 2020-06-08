from django.contrib import admin

# Register your models here.
from .models import BlogPost, Comment




@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	list_display=('title', 'slug', 'author', 'created')
	list_filter=( 'created','author')
	search_fields=('title', 'body')
	prepopulated_fields={'slug':('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display=('name', 'body', 'post')
	list_filter=('created', 'post')
	search_fields=('name', 'body',)