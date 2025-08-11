from django.shortcuts import render
import requests
from .forms import CityForm

def get_weather(request):
    weather_data = {}
    error = ""

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city'].strip().title()
            api_key = '2363191e3ca73c564e77af64ce2b578c'
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            # Debug prints
            print(f"Requesting weather for: {city}")
            print(f"Request URL: {url}")

            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
            print(f"Response Content: {response.text}")

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data.get('name', city),
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
            else:
                error = "City not found or API error. Please try again."
    else:
        form = CityForm()

    return render(request, 'weather.html', {'form': form, 'weather': weather_data, 'error': error})
