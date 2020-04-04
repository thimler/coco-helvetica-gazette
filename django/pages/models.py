from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "#" + self.name

class TextTestimonial(models.Model):
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
