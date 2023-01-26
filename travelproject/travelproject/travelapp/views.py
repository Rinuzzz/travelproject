# from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Person


# Create your views here.
# def demo(request):
#     name="india"
#     return render(request,"index1.html",{'obj':name})
# def about(request):
#     return render(request,"about.html")
# #
# # def contact(request):
# #     return HttpResponse("hello am contact")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})

def demo(request):
    obj = Place.objects.all()
    obj1= Person.objects.all()
    return render(request, "index.html", {'result': obj,'res':obj1})

