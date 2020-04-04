from django.db import models

GENDERS = [
    ("M", "Homme"),
    ("F", "Femme"),
    ("O", "Autre"),
]


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "#" + self.name


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
