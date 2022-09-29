from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.html import escape
from .models import Prospect, Contacteur
from services.models import Service


def contact(request):
    context = {}
    context["services"] = Service.objects.order_by("name")
    context["content"] = "contact d'un developpeur web et web designer"
    context["metadesc"] = "Avez vous besoin d'un developpeur web et/ou d'un designer ? Alors vous etes qu bon endroit. Prenez contact ici."
    return render(request, 'accounts/contact.html', context=context)


def contacter_signup(request):
    if request.POST:
        context = {}
        username = escape(request.POST.get("C_username"))
        email = escape(request.POST.get("C_email"))
        telephone = escape(request.POST.get("C_telephone"))
        message = escape(request.POST.get("C_message"))

        try:
            Contacteur.objects.create(username=username, email=email, telephone=telephone, content=message)
            Prospect.objects.create(username=username, email=email, telephone=telephone)
            context["contacter"] = Contacteur.username
            context["metadesc"] = 'ibavdigital'
            context["content"] = "ibavdigital"
            return render(request, 'vide.html', context=context)
        except:
            return HttpResponse("<script> alert('Une erreur est survenue veillez ressayer')</script>")

    return render(request, 'accounts/contact.html')
