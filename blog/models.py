from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    titre = models.CharField(max_length=150, unique=True, verbose_name='Titre')
    title = models.CharField(max_length=200, default='ibavdigital')
    meta_desc = models.CharField(max_length=500, default="Aujourd'hui, posséder un site web est indisssociable pour une entreprise car l'image que vous projetez sur le web est déterminante. C'est pourquoi, il est essentiel de disposer d'un site Internet attractif et fonctionnel")
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    image = models.ImageField(upload_to='image_article')
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(default='')

    def as_default(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre


class Actu(models.Model):
    titre = models.CharField(max_length=200)
    content = models.TextField()