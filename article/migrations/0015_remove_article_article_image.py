# Generated by Django 3.2 on 2021-05-16 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_remove_article_article_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_image',
        ),
    ]
