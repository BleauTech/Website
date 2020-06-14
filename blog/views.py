from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost
from taggit.models import Tag
from blog.form import CommentForm
from pprint import pprint
from django.contrib import messages

# Create your views here.


def post_list_view(request, tag_slug=None):
	posts=BlogPost.objects.all()
	tag=None
	all_tags=Tag.objects.all()
	if tag_slug :
		tag = get_object_or_404(Tag, slug=tag_slug)
		posts=BlogPost.objects.filter(tags__in=[tag])

	context={'posts':posts, 'tag':tag, 'all_tags':all_tags}
	return render(request, 'blog/blog.html', context)



def post_detail_view(request, pk):

	posts=BlogPost.objects.all()
	all_tags=Tag.objects.all()

	post=BlogPost.objects.filter(pk=pk).first()
	next_post=BlogPost.objects.filter(pk=pk+1).first()
	previous_post=BlogPost.objects.filter(pk=pk-1).first()
	commentform=CommentForm()
	
	if request.method=='POST':
		commentform=CommentForm(request.POST)
		if commentform.is_valid():
			pre_save_form=commentform.save(commit=False)
			pre_save_form.post=post
			pre_save_form.save()
			commentform=CommentForm()
			messages.success(request, 'your comment was saved successfully')
	


	context={'post':post,
			'previous_post':previous_post,
			'next_post':next_post,
			'posts':posts,
			'all_tags':all_tags,
			'commentform':commentform}

	return render(request, 'blog/single-blog1.html', context)




