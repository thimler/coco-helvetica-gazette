from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import TextTestimonial, Tag


class HomePageView(ListView):
    template_name = 'pages/home.html'
    model = TextTestimonial

class ArticleView(DetailView):
    model = TextTestimonial

class ByTagView(ListView):
    # TODO: Faire un nouveau template by tag ?
    template_name = 'pages/home.html'

    def get_queryset(self):
        return TextTestimonial.objects.filter(tags__pk=self.kwargs['pk'])
