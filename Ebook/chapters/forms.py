

from django import forms
#from pagedown.widgets import PagedownWidget
from pagedown.widgets import PagedownWidget
from .models import Chapter


class ChapterForm(forms.ModelForm):
	title = forms.CharField(initial="Untitled Chapter")

	content = forms.CharField(required=False, widget=PagedownWidget)
	class Meta :
		model = Chapter
		fields = [

			"title",
			"content",
			
		]
	