from django import forms
from datas.models import *
import random
import base64
import urllib.parse
import requests
from dotenv import load_dotenv
import os
load_dotenv()

def linkvertise(link):
    userid = 536896
    base_url = f"https://link-to.net/{userid}/{random.random() * 1000}/dynamic"
    href = f"{base_url}?r={base64.b64encode(link.encode('utf-8')).decode('utf-8')}"
    return href

def clictune(link):
    base_url = "https://www.clictune.com/Links_api/create_link?user_id=131475&api_key="+ os.getenv("CLICTUNEAPI_KEY") +"&url="
    full_url = base_url + urllib.parse.quote(link)
    r = requests.get(full_url)
    return r.json()['shortenedUrl']

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    discord = forms.CharField(max_length=50, required=True,label="Discord ID")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'discord', 'password1', 'password2')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        download = cleaned_data.get('download')
        download2 = cleaned_data.get('download2')
        if download2:
            modified_download2 = clictune(download2)
            cleaned_data['download2'] = modified_download2
        modified_download = clictune(download)
        cleaned_data['download'] = modified_download
        return cleaned_data


from django.utils.functional import lazy

def get_category_choices():
    return [(category.id, category.name) for category in Category.objects.all()]

lazy_category_choices = lazy(get_category_choices, list)

class CategoryForm(forms.Form):
    category = forms.ChoiceField(choices=lazy_category_choices)

