from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.


def post_list_view(request):
	posts=BlogPost.objects.all()

	context={'posts':posts}
	return render(request, 'blog/blog.html', context)

def post_detail_view(request, pk):
	print(slug)
	context={}
	return render(request, 'blog/single-blog.html', context)