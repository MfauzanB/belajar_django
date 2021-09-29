from collections import UserString
from coba.forms import BuatPesan
from django import forms
from django.shortcuts import redirect, render
from django import forms
from .models import bukutamu

def ListPesan(request):
    posts = bukutamu.objects.all()
    context = {
        'heading' : 'Pesan',
        'posts' : posts,
    }
    return render (request, 'coba/list_pesan.html',context)

def BuatPesan(request):
    form = bukutamu()

    context = {
        'form' : form
    }
    print(request.POST) 
    return render (request, 'coba/pesan.html', context )


    


    