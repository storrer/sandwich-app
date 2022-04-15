from django.shortcuts import render

from django.views import View
from django.http import Http404
import random

# Ingredients data dictionary
ingredients = {
    'meats': ['ham', 'salami', 'turkey', 'chicken', 'meatball', 'tempeh'],
    'cheeses': ['cheddar', 'provolone', 'swiss', 'american', 'gruyere', 'mozzarella'],
    'toppings': ['lettuce', 'tomato', 'pickles', 'onions', 'peppers'],
    'dough': ['hand tossed', 'thin crust', 'deep dish']
}

# Create your views here.
class SandwichappView(View):
    def get(self, request):
        # pass the keys to the ingredients dictionary to the template
        context = {'ingredients': ingredients.keys()}
        return render(request, 'sandwichapp.html', context=context)

class IngredientsView(View):
    def get(self, request, ingredient_type):
        if request.method == 'GET':
            if ingredient_type not in ingredients:
                raise Http404(f'No such ingredient: {ingredient_type}')

            return render(
                request = request,
                template_name = 'ingredients_list.html',
                context={ 'ingredients': ingredients[ingredient_type],
                            'ingredient_type': ingredient_type }
            )

class SandwichGeneratorView(View):
    pass