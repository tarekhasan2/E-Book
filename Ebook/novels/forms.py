


from django import forms
#from pagedown.widgets import PagedownWidget

from .models import Novel



class NovelCreate(forms.ModelForm):
	publish = forms.DateField(widget=forms.SelectDateWidget)

	# def __init__(self,*args, **kwargs):
	# 	super(NovelCreate, self).__init__(data=None, *args, **kwargs)

	# 	self.action = data.get('skip') if data else None

	# 	if self.action == 'Skip':
	# 		for field in self.fields:
	# 			field.required = False
	class Meta :
		model = Novel
		fields = [
			"image",
			"title",
			"description",
			"tags",
			"genre",
			"audience",
			"lenguage",
			"copyringt",
			"publish",

		]
	# def __init__(self, data=None, *args, **kwargs):
	# 	super(NovelCreate, self).__init__(data=data, *args, **kwargs)

	# 	# self.action = data.get('action') if data else None

	# 	if self.action == 'save':
	# 		for fields in self.fields:
	# 			fields.required = False
	
	

