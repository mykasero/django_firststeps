from django.shortcuts import render
# from django.http import HttpResponse lesson <4
from .models import Tour

# Create your views here.

# lesson <=6
# def index(request):
#     # return HttpResponse("First App") lesson <4
#     tours = Tour.objects.all()
#     context = {'tours' : tours}
#     return render(request, "tours/index.html", context)

#lesson >6
def index(request):
    return render(request, 'tours/index.html')