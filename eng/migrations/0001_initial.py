# Generated by Django 2.2.7 on 2019-11-07 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Category')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(default='We are Officially registered, Licensed, Insured and Experienced medical tourism agency. We make medical tourism Quick, Easy and Effortless since 2014. Contact us 24/7 and we will take care of everything', max_length=280)),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.CharField(max_length=280, verbose_name='Description')),
                ('content', models.TextField(verbose_name='Content')),
                ('img_link', models.CharField(default='static/cover_image_plaseholder.jpg', max_length=255, verbose_name='Cover image')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('slug', models.SlugField(unique=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='Published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eng.Category', verbose_name='Category')),
                ('keywords', models.ManyToManyField(to='eng.Keyword', verbose_name='Keywords')),
            ],
            options={
                'verbose_name': 'Article',
                'ordering': ['-created_on'],
            },
        ),
    ]
