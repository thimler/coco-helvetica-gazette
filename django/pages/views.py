from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import TextTestimonial, Tag


class HomePageView(ListView):
    template_name = "pages/home.html"
    model = TextTestimonial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class ArticleView(DetailView):
    model = TextTestimonial


class ByTagView(ListView):
    template_name = "pages/by_tag.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = get_object_or_404(Tag, pk=self.kwargs["pk"])
        return context

    def get_queryset(self):
        return TextTestimonial.objects.filter(tags__pk=self.kwargs["pk"])
