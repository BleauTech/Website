from django.db import models
from django.contrib.auth.models import User 
import datetime
from PIL import Image
from taggit.managers import TaggableManager


# Create your models here.



class BlogPost(models.Model):

	tags = TaggableManager()


	author=models.ForeignKey(User, 
		on_delete=models.CASCADE,
		 related_name='blog_post')
	title = models.CharField(max_length=255)
	slug = models.SlugField( unique=True)
	image = models.ImageField(blank=True, null=True, upload_to='blog_images')
	text = models.TextField()
	created = models.DateTimeField( auto_now_add=True)
	modified = models.DateTimeField( auto_now=True)
	class Meta:
		ordering=('-created',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[self.slug,])


	def save(self):
		super().save()

		img=Image.open(self.image.path)
		if img.height>300 or img.width>300:
			img.thumbnail((400,400))
			img.save(self.image.path)
 

# convinience function to get the month name
	def get_month_name(self):
		month_dict={'1':'Jan', '2':'Feb', '3':'Mar', '4':'Apr', '5':'May', '6':'Jun', '7':'Jul','8':'Aug','9':'Sept','10':'Oct','11':'Nov','12':'Dec'}
		month=str(self.created.month)
		month_name=month_dict.get(month)
		return month_name

# convinience methid for getting time delta
	def get_time_delta(self):
		present=datetime.datetime.now(datetime.timezone.utc)
		then=self.created
		delta=str(present-then)

		#split delta into days hrs and mins
		delta_to_list=delta.split(':')

		#if days and hrs equals 0 then use only minutes
		if delta_to_list[0]=='0':
			mins=delta_to_list[1]+' mins'
			return mins

		#else use days hours and mins
		hrs=delta_to_list[0]+' hrs'
		mins=delta_to_list[1]+' mins'
		total=hrs+' '+mins
	
		return total




class Comment(models.Model):
	post=models.ForeignKey(BlogPost, on_delete=models.CASCADE, 
		related_name='comments', null=True, blank=True)
	name=models.CharField(max_length=100)
	comment=models.TextField()
	email=models.EmailField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	


	class Meta:
		ordering=('-created',)

	def __str__(self):
		return f'comment by {self.name} on {self.post}'