from django.urls import path
from . import views

urlpatterns = [
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    # other paths...
]
