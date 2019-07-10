

from django import forms
#from pagedown.widgets import PagedownWidget

from .models import Chapter


class ChapterForm(forms.ModelForm):
	title = forms.CharField(initial="Untitled Chapter")

	content = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 20, 'cols':40}))
	class Meta :
		model = Chapter
		fields = [
			"image",
			#"video",
			"title",
			"content",
			
		]
	