from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Catalog(models.Model):
    topic = models.CharField(max_length=100)
    image = models.FileField(max_length=200, blank=True, null=True, verbose_name='konu Resmi')

    def __str__(self):
        return self.topic


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name='Yazar :')# auth.user tablosu ile ilişkilendirdirdik ve model CASCADE ile bir kullanıcı silinirse onunla ilişkili verilerde silinir.
    catalog = models.ForeignKey(Catalog, on_delete=models.DO_NOTHING, verbose_name='Konu', null=True)
    title = models.CharField(max_length=50, verbose_name='Başlık')
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True, verbose_name="Resim Yükleyin")

    def __str__(self):
        return self.title


class commentModel(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='makale', related_name='comments')
    comment_author = models.CharField(max_length=50, verbose_name='İsim')
    comment_context = models.CharField(max_length=100, verbose_name='Yorum')
    comment_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_context
