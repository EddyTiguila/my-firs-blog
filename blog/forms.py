from django import forms

from .models import Publicacion
class NuevoForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ('titulo', 'texto',)
