from django.db import models
from django.core.urlresolvers import reverse

class Tag(models.Model):
	name = models.CharField(max_length = 200)
	short_name = models.CharField(max_length = 20)
	description = models.TextField()

	def __unicode__(self): return self.name

	def get_absolute_url(self):
		return reverse('taglist')

class Post(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	author = models.CharField(max_length = 200)
	tag = models.ManyToManyField(Tag)
	status = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def get_absolute_url(self):
		return reverse('postlist')

class Comment(models.Model):
	content = models.TextField()
	author = models.CharField(max_length = 200)
	author_email = models.EmailField()
	status = models.BooleanField()
	created_at = models.DateTimeField()
	post = models.ForeignKey(Post)

