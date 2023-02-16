from dataclasses import fields
from pyexpat import model
from django import forms
from note.models import Contact

class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields={'name','email','mobno','message'}
