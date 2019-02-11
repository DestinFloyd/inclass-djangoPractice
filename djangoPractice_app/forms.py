from django import forms
from .models import Banana


class BananaForm(forms.ModelForm):

    class Meta:  # This Meta class is something you will see every now and then in Python.  It usually contains config info.
        model = Banana
        fields = ('color', 'name')
