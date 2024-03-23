from django.shortcuts import render

# Create your views here.
def getBillOfLading(request):
    info = request.GET.get('info')
