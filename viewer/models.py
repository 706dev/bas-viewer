from django.db import models
from django.urls import reverse


class content(models.Model):

    # Fields
    title = models.TextField(max_length=25)
    file = models.FileField(upload_to="content/")
    duration = models.DurationField(blank=10)
    specific_date = models.DateField(blank=True, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("viewer_content_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("viewer_content_update", args=(self.pk,))
