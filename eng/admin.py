from django.contrib import admin
from .models import Keyword, Category, Article

# Register your models here.

admin.site.register(Keyword)
admin.site.register(Category)
admin.site.register(Article)
