from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import JsonResponse
from django.views import View
from .models import Customers
# Create your views here.


def get_homeview(request: HttpRequest):
    """view function of index page"""
    if request.GET.get('valname'): 
            #if valname sent get the name
            valname = request.GET.get('valname')
            #get equivalent url from model
            url = Customers.objects.filter(person=valname).values("website")[0]['website'] 
            return JsonResponse({'urlLink':url},status=200) #return json response
    return render(request, "./templates/index.html")

def search_person(request):
    """everytime user inputs to search box, this function runs"""
    name = request.GET.get("name")
    namelist = []
    if name:
        #collect every objects that contains the input text
        customer_objects = Customers.objects.filter(person__icontains=name)
        for customer in customer_objects:
            namelist.append(customer.person)
    return JsonResponse({'status':200, 'name':namelist})
