from django.shortcuts import render

from .models import Pet
from django.http import Http404

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets,
    })

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404(f'The pet with id {pet_id} not match')
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })