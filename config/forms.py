from django import forms
from polls.models import PhoneModel
class PhoneForm(forms.ModelForm):
    name_uz = forms.CharField()
    name_ru = forms.CharField()
    name_en = forms.CharField()

    creator_name_uz = forms.CharField()
    creator_name_ru = forms.CharField()
    creator_name_en = forms.CharField()

    class Meta:
        model = PhoneModel
        exclude =('name','creator_name')