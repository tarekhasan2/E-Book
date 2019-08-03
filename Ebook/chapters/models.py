from django.db import models
from django.conf import settings
from django.urls import reverse

from markdown_deux import markdown
from django.utils.safestring import mark_safe
#from embed_video.fields import EmbedVideoField


def uploded_location(instance, filename):
	return "%s/%s" %(instance.id, filename)


class Chapter(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=True)
	title 		= models.CharField(max_length=120)
	content		= models.TextField()
	timestamp 	= models.DateTimeField(auto_now=False, auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True, auto_now_add=False)
	parent 		= models.IntegerField(null=True, blank=True)
	draft 		= models.BooleanField(default=True)



	def __unicode__(self):
		return str(self.title)



	def __str__(self):
		return self.title




	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)


	def get_absulte_url(self):
		return reverse("chapters:details" , kwargs={"id":self.id})
	

		
	# def next_chapter(self):
	# 	title = self.title
	# 	next_ = Chapter.objects.filter(title=title, id__gt=self.id).order_by('id').first()
	# 	return next_.id
