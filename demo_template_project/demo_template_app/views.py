from django.shortcuts import render
from .models import travel, travel_team


# Create your views here.
def index(request):
    obj1 = travel.objects.all()
    obj2 = travel_team.objects.all()
    return render(request, 'index.html', {'res1': obj1, 'res2': obj2})
    # return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def destination(request):
    return render(request,'destinations.html')
def element(request):
    return render(request,'elements.html')
def news(request):
    return render(request,'news.html')