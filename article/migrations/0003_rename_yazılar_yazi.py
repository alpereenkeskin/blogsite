# Generated by Django 3.2 on 2021-05-03 09:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_rename_articlemodel_yazılar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Yazılar',
            new_name='Yazi',
        ),
    ]
