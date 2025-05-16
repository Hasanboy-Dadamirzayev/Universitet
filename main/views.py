from re import search

from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import *
from .forms import *

def fanlar(request):
    fanlar = Fan.objects.all()

    if request.method == 'POST':
        Fan.objects.create(
            nom = request.POST.get('nom'),
            asosiy = True if request.POST.get('asosiy') == 'on' else False,
            yonalish = Yonalish.objects.get(id=request.POST.get('yonalish'))
        )

    search = request.GET.get('search')
    if search is not None:
        fanlar = Fan.objects.filter(nom__contains=search)
    else:
        fanlar = Fan.objects.all()

    context = {
        'fanlar': fanlar,
        'search': search,
        'yonalishlar': Yonalish.objects.all()
    }
    return render(request, 'fanlar.html', context)

def fan(request, fan_id):
    fan = Fan.objects.get(id=fan_id)
    context = {
        'fan': fan
    }
    return render(request, 'fan_confirm.html', context)

def yonalishlar(request):
    yonalishlar = Yonalish.objects.all()

    if request.method == 'POST':
        Yonalish.objects.create(
            nom = request.POST.get('nom'),
            aktiv = True if request.POST.get('aktiv') == 'on' else False,
        )

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

    if request.method == 'POST':
        Ustoz.objects.create(
            ism = request.POST.get('ism'),
            yosh = request.POST.get('yosh'),
            jins = request.POST.get('jins'),
            daraja = request.POST.get('daraja'),
            fan = Fan.objects.get(id=request.POST.get('fan'))
        )

    search = request.GET.get('search')
    if search is not None:
        ustozlar = Ustoz.objects.filter(ism__contains=search)
    else:
        ustozlar = Ustoz.objects.all()

    context = {
        'ustozlar': ustozlar,
        'search': search,
        'fanlar': Fan.objects.all(),
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

from django.shortcuts import get_object_or_404

def fan_edit(request, fan_id):
    fan = Fan.objects.get(id=fan_id)
    yonalishlar = Yonalish.objects.all()

    if request.method == 'POST':
        yonalish_id = request.POST.get('yonalish')
        yonalish = get_object_or_404(Yonalish, id=yonalish_id)

        fan.nom = request.POST.get('nom')
        fan.asosiy = 'asosiy' in request.POST
        fan.yonalish = yonalish
        fan.save()

        return redirect('fanlar')

    context = {
        'fan': fan,
        'yonalishlar': yonalishlar,
    }
    return render(request, 'fan_edit.html', context)

def yonalish_edit(request, yonalish_id):
    yonalish = Yonalish.objects.get(id=yonalish_id)
    if request.method == 'POST':
        Yonalish.objects.filter(id=yonalish_id).update(
            nom = request.POST.get('nom'),
            aktiv = True if request.POST.get('aktiv') == 'on' else False
        )
        return redirect('yonalishlar')
    context = {
        'yonalish': yonalish
    }
    return render(request, 'yonalish_edit.html', context)

def ustoz_edit(request, ustoz_id):
    ustoz = Ustoz.objects.get(id=ustoz_id)
    fanlar = Fan.objects.all()
    if request.method == 'POST':
        Ustoz.objects.filter(id=ustoz_id).update(
            ism = request.POST.get('ism'),
            yosh = request.POST.get('yosh'),
            jins =  request.POST.get('jins'),
            daraja = request.POST.get('daraja'),
            fan = request.POST.get('fan'),
        )
        return redirect('ustozlar')
    context = {
        'ustoz': ustoz,
        'jinslar': Ustoz.JINS_TANLASH,
        'darajalar': Ustoz.DARAJA,
        'fanlar': fanlar,
    }
    return render(request, 'ustoz_edit.html', context)

def fan_create(request):
    if request.method == 'POST':
        form_data = FanForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('fanlar')
    context = {
        'form': FanForm,
    }
    return render(request, 'fan_create.html', context)

def yonalish_create(request):
    if request.method == 'POST':
        form_data = YonalishForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('yonalishlar')

    context = {
        'form': YonalishForm,
    }
    return render(request, 'yonalish_create.html', context)

def ustoz_create(request):
    if request.method == 'POST':
        form_data = UstozForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('teachers')

    context = {
        'form': UstozForm,
    }
    return render(request,'ustoz_create.html', context)



