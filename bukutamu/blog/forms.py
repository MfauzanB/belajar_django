from django import forms


class PostForm(forms.Form):
	nama		= forms.CharField(max_length = 20)
	pesan		= forms.CharField(
		widget = forms.Textarea
		)