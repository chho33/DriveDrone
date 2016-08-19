from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def frontPage(request):
    return render(request, 'webapp/index.html')

@csrf_exempt
def delivery(request):
    data = request.POST 
    names = data['names']
    imgs = data['imgs']
    prices = data['prices']
    amounts = data['amounts']
    return render(request, 'webapp/delivery.html',locals())
