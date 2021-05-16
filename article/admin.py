from django.contrib import admin
from .models import Article,commentModel,Catalog
# Register your models here.
admin.site.register(Article)
admin.site.register(commentModel)
admin.site.register(Catalog)