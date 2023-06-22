from django import forms
from datas.models import *

class CategoryForm(forms.Form):
    category_choices = [(category.id, category.name) for category in Category.objects.all()]
    category = forms.ChoiceField(choices=category_choices)
