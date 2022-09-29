from django.shortcuts import render
from .models import Article, Actu
from services.models import Service


def BlogHome(request):
    context = {}
    context["posts"] = Article.objects.filter(published=True)
    context["services"] = Service.objects.order_by('name')
    context["actu"] = Actu.objects.get()
    context["content"] = "Articles de blog d'informatique"
    context["metadesc"] = "Tous les articles qui vous aideront a tout connaitre et a ameliorer vos connaissances sur le monde de l'informatique et en particulier celui du web et du design"
    return render(request, 'blog/blog.html', context=context)


def article_post(request, slug):
    context = {}
    post = Article.objects.get(slug=slug)
    context["article"] = post
    context["services"] = Service.objects.order_by('name')
    context["content"] = post.title
    context["metadesc"] = post.meta_desc
    return render(request, 'blog/article_blog.html', context=context)
