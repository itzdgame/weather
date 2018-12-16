from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse

def get_weather(request):
    location = request.GET.get("location")
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + str(location) + '&appid=a4702307e95e36ff32fa85fac5eab619')
    return HttpResponse(JsonResponse(r.json()))

def index(request):
    return render(request, "showtemp/index.html")