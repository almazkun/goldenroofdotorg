from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse

import markdown


class Keyword(models.Model):
    name = models.CharField("Keyword", max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Category", max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField(
        max_length=280, default=settings.SITE_DESCRIPTION
    )  # SEO head meta tag Description for a category page

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("eng:category", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]


class Article(models.Model):
    IMG_LINK = "/images/cover_image_plaseholder.jpg"
    title = models.CharField(verbose_name="Title", max_length=255)
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Description", max_length=280)
    content = models.TextField(verbose_name="Content", help_text="Use Markdown syntax")
    img_link = models.CharField(
        verbose_name="Cover image", default=IMG_LINK, max_length=255
    )
    created_on = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name="Updated", auto_now=True)
    views = models.IntegerField(verbose_name="Views", default=0)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField("Published", default=False)

    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.PROTECT
    )
    keywords = models.ManyToManyField(Keyword, verbose_name="Keywords")

    class Meta:
        verbose_name = "Article"
        ordering = ["-created_on"]

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse("eng:article_detail", kwargs={"slug": self.slug})

    def update_views(self):
        self.views += 1
        self.save(update_fields=["views"])

    def contetn_to_markdown(self):
        return markdown.markdown(self.content, extensions=["markdown.extensions.extra"])


class EmailRequest(models.Model):
    created_on = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    name = models.EmailField()
    answered = models.BooleanField(verbose_name="Answered", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"
        ordering = ["created_on"]
