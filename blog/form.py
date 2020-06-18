from django.forms import ModelForm
from blog.models import Comment


# Create the form class.


class CommentForm(ModelForm):

	class Meta:
		model = Comment
		fields = ['post', 'name', 'email', 'comment']