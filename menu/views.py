from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


def index(request):
    """pizzas = Pizza.objects.all()
    pizza_names_and_prices = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizzas_names_and_prices_str = ", ".join( pizza_names_and_prices)
    return HttpResponse("Les pizzas: " + pizzas_names_and_prices_str)"""
    pizzas = Pizza.objects.all().order_by("prix")
    return render(request, 'menu/index.html', {'pizzas': pizzas})
