from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .models import TextTestimonial, Tag
from django.forms import modelform_factory

ArticleCreate = modelform_factory(
    TextTestimonial, fields=["text", "author_gender", "author_age"]
)


class HomePageView(ListView):
    template_name = "pages/home.html"
    model = TextTestimonial
    fields = ("text",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["ArticleCreate"] = ArticleCreate
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


def manage_articles(request):
    if request.method == "POST":
        form = ArticleCreate(request.POST, request.FILES)
        form.save()
    return redirect("home")
