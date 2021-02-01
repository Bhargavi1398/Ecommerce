from django import forms
from testapp.models import Conformation

class ConformationForm(forms.ModelForm):

    class Meta:
        model=Conformation
        fields="__all__"
