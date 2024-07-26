from django.shortcuts import render , redirect # redirect lesson 7
# from django.http import HttpResponse lesson <4
# from .models import Tour lesson 4-7
from .forms import ContactForm #lesson 7

# Create your views here.

# lesson <=6
# def index(request):
#     # return HttpResponse("First App") lesson <4
#     tours = Tour.objects.all()
#     context = {'tours' : tours}
#     return render(request, "tours/index.html", context)

#lesson 7
# def index(request):
#     return render(request, 'tours/index.html')

#lesson 8
#home page view function
def home_view(request):
    return render(request, 'tours/home.html')

#contact form handling function
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()

    context = {'form' : form}
    return render(request, 'tours/contact.html', context)

#success page

def success_view(request):
    return render(request, 'tours/success.html')



