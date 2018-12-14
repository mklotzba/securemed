from django import forms
from .models import Ise


class IseForm(forms.ModelForm):
	class Meta:
		model = Ise
		exclude = []
