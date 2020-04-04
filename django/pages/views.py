from django.views.generic import ListView
from .models import TextTestimonial


class HomePageView(ListView):
    template_name = 'pages/home.html'
    model = TextTestimonial
