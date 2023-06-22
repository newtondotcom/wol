from django import forms
from datas.models import *
import random
import base64

def linkvertise(link):
    userid = 536896
    base_url = f"https://link-to.net/{userid}/{random.random() * 1000}/dynamic"
    href = f"{base_url}?r={base64.b64encode(link.encode('utf-8')).decode('utf-8')}"
    return href

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        download = cleaned_data.get('download')
        download2 = cleaned_data.get('download2')
        if download2:
            modified_download2 = linkvertise(download2)
            cleaned_data['download2'] = modified_download2
        modified_download = linkvertise(download)
        cleaned_data['download'] = modified_download
        return cleaned_data


