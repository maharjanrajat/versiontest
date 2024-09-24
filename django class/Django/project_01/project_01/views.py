#from dango.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, 'home.html')
#   return HttpResponse("Hello World")

def about(request):
    return render(request, 'about.html')
#   return Htpresponse("My")