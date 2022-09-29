from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, default='ibavdigital')
    slug = models.SlugField()
    image = models.ImageField(upload_to='image_cat')
    description = models.TextField(null=True, blank=True)

    def as_default(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=100, default='vide')
    slug = models.SlugField(default='ibav')
    title = models.CharField(max_length=200, default='ibavdigital')
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def as_default(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Commande(models.Model):
    projet = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='')
    slug = models.SlugField()
    namecompany = models.CharField(max_length=100)
    email_user = models.EmailField()
    description = models.TextField()
    tel = models.CharField(max_length=20, default='------------')
    budget = models.IntegerField(blank=True, null=True)

    def as_default(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Terms(models.Model):
    title = models.CharField(max_length=200, default='ibavdigital')
    content = models.TextField()