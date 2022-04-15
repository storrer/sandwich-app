from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsView, SandwichGeneratorView

urlpatterns = [
    # Main Sandwich app page
    path('', SandwichappView.as_view(), name='sandwich'),
    # Ingredient list page
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list'),
    # Random sandwich generation page
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator'),
]
