from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.list, name='articles'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('detay/<int:id>', views.detail, name='detail'),
    path('makaleekle', views.AddArticle, name="addarticle"),
    path('makalegüncelle/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('addComment/<int:id>', views.addcomment, name='addcomment'),
    path('yazılım', views.sortBysofware, name="software"),
    path('mimarirestorasyon', views.sortByengineer, name="engineer"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
