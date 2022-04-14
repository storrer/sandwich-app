from django.shortcuts import render

from django.views import View
import random
ingredients = {
    'meats': ['ham', 'salami', 'turkey', 'chicken', 'meatball', 'tempeh'],
    'cheeses': ['cheddar', 'provolone', 'swiss', 'american', 'gruyere'],
    'toppings': ['lettuce', 'tomato', 'pickles', 'onions', 'peppers'],
    'dough': ['hand tossed', 'thin crust', 'deep dish']
}

# Create your views here.
class SandwichappView(View):
    def get(self, request):
        return render(request, 'sandwichapp.html')
class SandwichGenerator(View):
    def get(self,reqiest):
        return
# create view for sandwich, view for generated sandwich, and the html page for the sandwich generator