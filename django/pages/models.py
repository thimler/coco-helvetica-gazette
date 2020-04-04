from django.db import models

# Create your models here.
class TextTestimonial(models.Model):
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
