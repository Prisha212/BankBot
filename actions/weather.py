import requests

def Weather(city):
  
    api_address ='https://api.openweathermap.org/data/2.5/weather?appid=e1ba218358d49fa7f1febfba4a6522fa&q='
    city = input('Enter the City name :')
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['main']
    print(format_add)
    print("Weather is {0} Temperature is minimum {1} Celsius and maximum is {2} celsius.".format(
    json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
    return format_add
    