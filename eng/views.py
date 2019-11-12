from django.shortcuts import render
from django.views import generic

from .models import Keyword, Category, Article
from .forms import send_email


from django.core.exceptions import ValidationError
from django.core.validators import validate_email


import markdown


def homepage_view(request):
    if "email_request" in request.POST:
        email_request = request.POST["email_request"]
        print(email_request)
        print(validate_email(email_request))
        if validate_email(email_request):
            try:
                print(email_request)
                send_email(email_request)
                return render(request, "succes.html")
            except:
                return render(request, "unsucces.html")
        else:
            return render(request, "badsucces.html")
        
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
