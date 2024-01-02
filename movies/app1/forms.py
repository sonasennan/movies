from django import forms
from app1.models import Movie


#form definition
class MovieForm(forms.ModelForm):

    class Meta:

        model=Movie

        fields="__all__"