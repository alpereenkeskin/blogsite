# Generated by Django 3.2 on 2021-05-03 09:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleModel',
            new_name='Yazılar',
        ),
    ]
