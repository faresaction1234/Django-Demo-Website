from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexpage(request):
    return render(request, 'dar/index.html')
    #return HttpResponse('<h1>welcome to the home page</h1>')
def about_us(request):
    nigga = [5, 7, 7]
    dict_data = {
        'Fullname': 'Mohamed fares Ben Ayed',
        'age': 23,
        'address': 'med.fares.ben.ayed1997@gmail.com',
        'points': nigga,
    }
    return render(request, 'dar/aboutus.html', context=dict_data)
    #return HttpResponse('<h1>About us</h1>')
def contact_us(request):
    return render(request, 'dar/contactus.html')
    #return HttpResponse('<h1>Contact us</h1>')
