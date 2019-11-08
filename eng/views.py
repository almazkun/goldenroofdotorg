from django.shortcuts import render
from django.views import generic

from .models import Keyword, Category, Article


import markdown


def homepage_view(request):
    return render(request, "home.html")


class ListView(generic.ListView):
    model = Article
    template_name = "articles.html"
    context_object_name = "articles"


class DetailView(generic.DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"

    def get_object(self):
        obj = super(DetailView, self).get_object()
        obj.update_views()

        md = markdown.Markdown(extensions=["markdown.extensions.extra"])
        obj.content = md.convert(obj.content)

        return obj
