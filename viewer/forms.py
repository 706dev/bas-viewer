from django import forms
from . import models


class contentForm(forms.ModelForm):
    class Meta:
        model = models.content
        fields = [
            "specific_date",
            "file",
            "title",
            "duration",
        ]
