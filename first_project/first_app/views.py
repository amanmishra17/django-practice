from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# print('hello welcome to django')
def home2(request):
    return HttpResponse("aman is good boy")
