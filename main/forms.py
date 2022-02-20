from dataclasses import fields
from django import forms
from main import models


class InsertForm(forms.ModelForm):
    class Meta:
        model=models.Personal
        fields="__all__"


class MarkForm(forms.ModelForm):
    class Meta:
        model=models.Mark
        exclude=('total',)