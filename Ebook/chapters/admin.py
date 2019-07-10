from django.contrib import admin

# Register your models here.


from .models import Chapter

class ChapterModelAdmin(admin.ModelAdmin):

	class Meta:
		model = Chapter

admin.site.register(Chapter, ChapterModelAdmin)


