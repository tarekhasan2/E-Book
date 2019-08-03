from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.urls import reverse
from chapters.models import Chapter
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

AUDIENCE_STATUS_CHOICES = (
		('primary', 'Who is your primary audience?'),
		('middle', 'Middle Grade (8-13 years of age)'),
		('young', 'Young Adult(13-18 years of age)'),
		('adult', 'Adult(25+ years of age)'),
	)
LENGUAGE_STATUS_CHOICES = (
		('created', 'Created'),
		('paid', 'Paid'),
		('shipped', 'Shipped'),
		('refunded', 'Refunded'),
	)


COPYRIGHT_STATUS_CHOICES = (
		('not_specified', 'Not Specified'),
		('reserved', 'All Right Reserved'),
		
	)




def uploded_location(instance, filename):
	return "%s/%s" %(instance.id, filename)





class Novel(models.Model):
	user		= models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=True)
	title		= models.CharField(max_length=120, default='Untaiteld')
	image 		= models.FileField(upload_to = uploded_location, null=True, blank=True)
	description = models.TextField()
	genre		= models.CharField(max_length=120, default='select a genre', choices= GENRE_STATUS_CHOICES)
	audience	= models.CharField(max_length=120, default='primary', choices= AUDIENCE_STATUS_CHOICES)
	lenguage	= models.CharField(max_length=120, default='created', choices= LENGUAGE_STATUS_CHOICES)
	copyringt	= models.CharField(max_length=120, default='not_specified', choices= COPYRIGHT_STATUS_CHOICES)
	drafted 	= models.BooleanField(default=True)
	timestamp 	= models.DateTimeField(auto_now=False, auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True, auto_now_add=False)
	publish 	= models.DateField(auto_now=False, auto_now_add= False)
	tags		= TaggableManager()
	rate 		= models.CharField(max_length=120, default='Untaiteld')
	


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

	def children(self):
		return Chapter.objects.filter(parent=self.id)


	def published(self):
		return Chapter.objects.filter(parent=self.id, draft=False)

	def draft(self):
		return Chapter.objects.filter(parent=self.id, draft=True)

