from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    city = requests.GET.get('city', 'Delhi')
    #city ="Delhi"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ef30ebca6ebcab61e960146be2b18900"
    data = requests.get(url).json()
   # print(data)

    payload = {'city': data['name'],
             'weather': data['weather'][0]['main'],
             'icon': data['weather'][0]['icon'],
             'kelvin_temperature': data['main']['temp'],
             'celcius_temperature': data['main']['temp'] - 273,
             'pressure':data['main']['pressure'],
             'humidity':data['main']['humidity'],
             'description':data['weather'][0]['description']
             }
    context ={'data': payload}
    print(context)
    return render(request,'home.html')
