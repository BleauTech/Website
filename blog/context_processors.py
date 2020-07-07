from blog.models import BlogPost

def blog_post_processor(request):
    all_posts=BlogPost.objects.all()[:3]
    context={'all_posts':all_posts}
    return context

