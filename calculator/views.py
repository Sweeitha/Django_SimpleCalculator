from django.shortcuts import render

def calc(request):
    return render(request, 'calc/calculate.html')
# Create your views here.
