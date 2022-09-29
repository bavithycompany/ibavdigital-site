from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import context
from django.utils.html import escape
from django.utils.text import slugify

from .models import Service, Commande, Portfolio, Terms
from accounts.models import Prospect


def index(request):
    context = {}
    context["services"] = Service.objects.order_by("name")
    context["portfolio"] = Portfolio.objects.order_by('description')
    return render(request, 'index.html', context=context)


def devis(request):
    context = {}
    context["services"] = Service.objects.order_by("name")
    context["content"] = "Devis d'une conception web/design"
    context["metadesc"] = "Confiez la conception de votre site web et de vos visuels a un professionnel pour une meilleur presence web"
    return render(request, 'services/devis.html', context=context)


def portfolio(request):
    context = {}
    content = Portfolio.objects.all()
    service = Service.objects.order_by("name")
    context["portfolio"] = content
    context["services"] = service
    context["content"] = content[1].title
    context["metadesc"] = "Quelques realisations d'un web concepteur/designer"
    return render(request, 'services/portfolio.html', context=context)


def get_page_service(request, slug):
    context = {}
    service = Service.objects.get(slug=slug)
    context["service"] = service
    context["services"] = Service.objects.order_by("name")
    context["content"] = service.title
    context["metadesc"] = service.description
    return render(request, 'services/service_details.html', context=context)


def commande(request):
    if request.POST:
        context = {}
        projet = escape(request.POST.get("projet"))
        username = escape(request.POST.get("name"))
        email = escape(request.POST.get("email"))
        description = escape(request.POST.get("message"))
        namecompany = escape(request.POST.get("companyName"))
        budget = escape(request.POST.get("budget"))
        tel = escape(request.POST.get("phone"))
        commande_, _ = Commande.objects.get_or_create(projet=projet, username=username, namecompany=namecompany,
                                                      budget=budget, tel=tel, email_user=email,
                                                      description=description, slug=slugify(username))
        Prospect.objects.create(username=username, email=email, telephone=tel)
        context["contacter"] = commande_
        context["metadesc"] = 'ibavdigital'
        context["content"] = "ibavdigital"
        return render(request, 'vide.html', context=context)
    return render(request, 'services/devis.html')


def terms_of_use(request):
    context = {}
    context["content"] = "ibavdigital"
    context["term"] = Terms.objects.get()
    context["services"] = Service.objects.order_by("name")
    context["metadesc"] = "conditions d'utilisation du site web ibavdigital"
    return render(request, 'condition_of_use.html', context=context)