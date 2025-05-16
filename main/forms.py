from django import forms
from .models import *

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = '__all__'

class YonalishForm(forms.ModelForm):
    class Meta:
        model = Yonalish
        fields = '__all__'

class UstozForm(forms.ModelForm):
    class Meta:
        model = Ustoz
        fields = '__all__'