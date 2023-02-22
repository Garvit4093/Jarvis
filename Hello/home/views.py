from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello this is GARVIT")
def about(request):
    return HttpResponse("Hello this is GARVIT GUPTA")