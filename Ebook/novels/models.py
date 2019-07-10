from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.urls import reverse

from markdown_deux import markdown
from django.utils.safestring import mark_safe
# Create your models here.

GENRE_STATUS_CHOICES = (
		('select a genre', 'Select a genre'),
		('action', 'Action'),
		('adventure', 'Adventure'),
		('chicklit', 'Chicklit'),
		('fanfiction', 'Fanfiction'),
		('fantacy', 'Fantacy'),
		('general fiction', 'General Fiction'),
		('historical fiction', 'Historical Fiction'),
		('horror', 'Horror'),
		('humor', 'Humor'),
		('mystry/thriller', 'Mystry/Thriller'),
		('non-fiction', 'Non-fiction'),
		('paranonmal', 'Paranonmal'),
		('poetry', 'Poetry'),
		('random', 'Random'),
		('romance', 'Romance'),
		('science fiction', 'Science Fiction'),
		('short story', 'Short Story'),
		('spiritual', 'Spiritual'),
		('teen fiction', 'Teen Fiction'),
		('vampire', 'Vampire'),
		('werewolf', 'Werewolf'),

	)
ORDER_STATUS_CHOICES = (
		('created', 'Created'),
		('paid', 'Paid'),
		('shipped', 'Shipped'),
		('refunded', 'Refunded'),
	)
AUDIENCE_STATUS_CHOICES = (
		('created', 'Created'),
		('paid', 'Paid'),
		('shipped', 'Shipped'),
		('refunded', 'Refunded'),
	)
LENGUAGE_STATUS_CHOICES = (
		('created', 'Created'),
		('paid', 'Paid'),
		('shipped', 'Shipped'),
		('refunded', 'Refunded'),
	)


COPYRIGHT_STATUS_CHOICES = (
		('created', 'Created'),
		('paid', 'Paid'),
		('shipped', 'Shipped'),
		('refunded', 'Refunded'),
	)




def uploded_location(instance, filename):
	return "%s/%s" %(instance.id, filename)


class Novel(models.Model):
	user		= models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=True)
	title		= models.CharField(max_length=120, default='Untaiteld')
	image 		= models.ImageField(upload_to = uploded_location, null=True, blank=True)
	description = models.TextField()
	genre		= models.CharField(max_length=120, default='select a genre', choices= GENRE_STATUS_CHOICES)
	audience	= models.CharField(max_length=120, default='created', choices= AUDIENCE_STATUS_CHOICES)
	lenguage	= models.CharField(max_length=120, default='created', choices= LENGUAGE_STATUS_CHOICES)
	copyringt	= models.CharField(max_length=120, default='created', choices= COPYRIGHT_STATUS_CHOICES)
	publish 	= models.DateField(auto_now=False, auto_now_add=False)
	timestamp 	= models.DateTimeField(auto_now=False, auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True, auto_now_add=False)
	draft 		= models.BooleanField(default=True)
	rating		= models.BooleanField(default=False)
	tags		= TaggableManager()


	class Meta:
		ordering = ["-publish"]



	def __unicode__(self):
		return str(self.title)

	def __str__(self):
		return self.title

	def get_markdown(self):
		content = self.description
		markdown_text = markdown(content)
		return mark_safe(markdown_text)

	def get_absulte_url(self):
		return reverse("novels:details" , kwargs={"id":self.id})