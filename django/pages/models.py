from django.db import models
from django.utils.translation import ugettext_lazy as _
from .tags import ALLOWED_TAGS
from django.urls import reverse


GENDERS = [
    ("M", _("Homme")),
    ("F", _("Femme")),
    ("O", _("Autre")),
]


class Tag(models.Model):
    name = models.CharField(max_length=200, choices=ALLOWED_TAGS)

    def __str__(self):
        return self.get_name_display()


class TextTestimonial(models.Model):
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    author_age = models.IntegerField(blank=True, null=True)
    author_gender = models.CharField(
        max_length=1, choices=GENDERS, null=True, blank=True
    )

    def __str__(self):
        return '"' + " ".join(self.text.split()[:5]) + '"'

    def get_absolute_url(self):
        return reverse("article", kwargs={"pk": self.pk})
