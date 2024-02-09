from asyncio.windows_events import NULL
from uuid import RFC_4122
from django.shortcuts import render, redirect
from .models import Challenge, Submission, Judge, Critic
from .forms import CriticForm
from django.http import JsonResponse
import  json
from django.db.models import Q
from django.db.models import fields
from django.db import connection

def display_sub(request):
    submission=Submission.objects.all()
    return render(request,"disp_sub.html",{"S1":submission})



def display_criti(request):
    criti=Critic.objects.all()
    return render(request,"disp_criti.html",{"CR1":criti})

def add_critic(request):
    if request.method == 'POST':
        form = CriticForm(request.POST)
        if form.is_valid():
            form.save()
            form = CriticForm()
            mssg="done"
            # return redirect("listing") # redirection vers la page de l’url: listing
        return render(request,"add_critic.html",{"form":form,"message":mssg})
    else:
        form = CriticForm() #créer une instance de formulaire vierge
        mssg ="veuillez remplir tous les champs"
        return render(request,"add_critic.html",{"form":form,"message":mssg})
