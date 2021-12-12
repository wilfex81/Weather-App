import pip._vendor.requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3557d39e65afabb80d400958d43d6b14'

    if request.method == 'POST':
        pass
    
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = pip._vendor.requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
           'temperature': r ['main']['temp'] ,
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    
    return render(request, 'weather/weather.html', context)