


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from django import forms
#from pagedown.widgets import PagedownWidget

from .models import Novel
from html.parser import HTMLParser


class NovelCreate(forms.ModelForm):
	
	publish = forms.DateField(widget=forms.SelectDateWidget)
	# def __init__(self,*args, **kwargs):
	# 	super(NovelCreate, self).__init__(data=None, *args, **kwargs)

	# 	self.action = data.get('skip') if data else None

	# 	if self.action == 'Skip':
	# 		for field in self.fields:
	# 			field.required = False

	#image = forms.ImageField(required=False, onchange="upload_img(this)")
	#image = forms.FileField(required=False, widget=forms.FileInput(attrs={'id':'imgInp'}))
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

	def __init__(self, *args, **kwargs):
		super(NovelCreate, self).__init__(*args, **kwargs)
		self.fields['image'].widget.attrs.update({
		   'id': 'imgInp',
		})
		self.helper = FormHelper(self)
		self.helper.form_tag = False
		self.helper.disable_csrf = True
		self.helper.layout = Layout(
			'imagefile',
            HTML("""{% if form.imagefile.value %}<img class="img-responsive" src="{{ MEDIA_URL }}{{ form.imagefile.value }}">{% endif %}""", ),
            'flag_featured',
        )




        
	# def __init__(self, data=None, *args, **kwargs):
	# 	super(NovelCreate, self).__init__(data=data, *args, **kwargs)

	# 	# self.action = data.get('action') if data else None

	# 	if self.action == 'save':
	# 		for fields in self.fields:
	# 			fields.required = False
	
	

