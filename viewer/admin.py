from django.contrib import admin
from django import forms

from . import models


class contentAdminForm(forms.ModelForm):

    class Meta:
        model = models.content
        fields = "__all__"


class contentAdmin(admin.ModelAdmin):
    form = contentAdminForm
    list_display = [
        "title",
        "file",
        "specific_date",
        "duration",
    ]


admin.site.register(models.content, contentAdmin)
