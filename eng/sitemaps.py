from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from .models import Article


class StaticViewSitemap(Sitemap):
    def items(self):
        return ["home", "articles"]

    def location(self, item):
        return reverse(item)


class ArticleSitemap(Sitemap):
    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.created_on
