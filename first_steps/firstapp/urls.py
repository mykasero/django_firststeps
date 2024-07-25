from django.urls import path
from .views import index

# Define a list of url patterns

urlpatterns = [
    path('', index, name="index"),
]

