from django import form
from . import models

class CreateArticles(forms.ModelForm):
    class meta:
        model = models.article
        fields = ['title', 'body', 'slug', 'thumb']