from django.urls import path
from sandwichapp.views import SandwichappView

urlpatterns = [
    path('', SandwichappView.as_view(), name='sandwich'),
]
