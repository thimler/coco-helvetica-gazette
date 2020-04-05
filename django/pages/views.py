from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import TextTestimonial, Tag
from django.forms import modelform_factory


class HomePageView(ListView):
    template_name = "pages/home.html"
    model = TextTestimonial
    fields = ("text", "tags", "author_age", "author_gender")
    ArticleCreate = modelform_factory(TextTestimonial, fields=fields)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["ArticleCreate"] = self.ArticleCreate
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
    fields = ("text", "tags", "author_age", "author_gender")
    ArticleCreate = modelform_factory(TextTestimonial, fields=fields)
    if request.method == 'POST':
        form = ArticleCreate(request.POST, request.FILES)
        form.save()
    else:
        form = ArticleCreate()
    return render(request, 'pages/home.html')

