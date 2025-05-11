from re import search

from django.shortcuts import render, redirect
from .models import *

def fanlar(request):
    fanlar = Fan.objects.all()

    search = request.GET.get('search')
    if search is not None:
        fanlar = Fan.objects.filter(nom__contains=search)
    else:
        fanlar = Fan.objects.all()

    context = {
        'fanlar': fanlar,
        'search': search
    }
    return render(request, 'fanlar.html', context)

def fan(request, fan_id):
    fan = Fan.objects.get(id=fan_id)
    context = {
        'fan': fan
    }
    return render(request, 'fan_confirm.html', context)

def fan_delete(request, fan_id):
    fan = Fan.objects.get(id=fan_id)
    fan.delete()
    return redirect('fanlar')

def yonalishlar(request):
    yonalishlar = Yonalish.objects.all()
    context = {
        'yonalishlar': yonalishlar
    }
    return render(request, 'yonalishlar.html', context)

def yonalish_delete(request, yonalish_id):
    yonalish = Yonalish.objects.get(id=yonalish_id)
    yonalish.delete()
    return redirect('yonalishlar')

def yonalish_confirm(request, yonalish_id):
    yonalish = Yonalish.objects.get(id=yonalish_id)
    context = {
        'yonalish': yonalish
    }
    return render(request, 'yonalish_confirm.html', context)

def ustozlar(request):
    ustozlar = Ustoz.objects.all()

    search = request.GET.get('search')
    if search is not None:
        ustozlar = Ustoz.objects.filter(ism__contains=search)
    else:
        ustozlar = Ustoz.objects.all()

    context = {
        'ustozlar': ustozlar,
        'search': search
    }
    return render(request, 'ustozlar.html', context)

def ustoz_delete(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)
    ustoz.delete()
    return redirect('ustozlar')


def ustoz_confirm(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)
    context = {
        'ustoz': ustoz
    }
    return render(request, 'usoz_confirm.html', context)



