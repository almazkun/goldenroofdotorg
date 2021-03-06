# Generated by Django 2.2.7 on 2019-11-13 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("eng", "0005_emailrequest")]

    operations = [
        migrations.AlterModelOptions(
            name="emailrequest",
            options={
                "ordering": ["created_on"],
                "verbose_name": "email",
                "verbose_name_plural": "Emails",
            },
        ),
        migrations.RenameField(
            model_name="emailrequest", old_name="email", new_name="name"
        ),
    ]
