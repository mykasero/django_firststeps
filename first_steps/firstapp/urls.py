from django.urls import path
# from .views import index #lesson <=6
from . import views
# Define a list of url patterns

urlpatterns = [
    path('', views.home, name="homepage"),
    path('contact/', views.contact_view, name = 'contact_view'),
    path('contact/', views.success_view, name = 'contact-success'),
]

