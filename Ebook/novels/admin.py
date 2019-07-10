from django.contrib import admin

# Register your models here.


from .models import Novel

class BlogModelAdmin(admin.ModelAdmin):

	class Meta:
		model = Novel

admin.site.register(Novel, BlogModelAdmin)