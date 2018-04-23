"""
Get the weather/forecast from another API.  This API might be deprecated because of how old this script is, but if
it isnt, Hurrah!
"""
import json
import requests
import datetime

headers = {'user-agent': 'Mozilla/5.0'}
APIKEY = '&APPID=c2f8dc4a130e054c8e09311bd82ce712'
naperville_Code  ='id=4903279'
imperial = '&units= imperial'
weather_type = ['weather?', 'forecast?']
weather_url = 'http://api.openweathermap.org/data/2.5/'

def cur_weather():
    weather_data = requests.get(weather_url + weather_type[0]+ naperville_Code + APIKEY + imperial, headers= headers)
    weather_json = weather_data.json()

    sunrise_unix = weather_json['sys']['sunrise']
    sunset_unix = weather_json['sys']['sunset']
    sunrise = datetime.datetime.fromtimestamp(sunrise_unix).strftime('%H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(sunset_unix).strftime('%H:%M:%S')

    weather = weather_json['weather'][0]['description']
    cur_temp = weather_json['main']['temp'] - 273
    cur_humid = weather_json['main']['humidity']
    print "The current weather is %s" %(weather)
    print "The current temp is %.2f and the humidity is %.2f"% (cur_temp, cur_humid)
    print "The sunrise is at %s AM and the sunset is at %s" %(sunrise, sunset)

def five_Forecast():
    weather_forecast = requests.get(weather_url + weather_type[1] + naperville_Code + APIKEY + imperial)
    w_f_json = weather_forecast.json()
    i = 1
    weather = []
    while i< len(w_f_json['list']):
        wf_dict = w_f_json['list'][i]
        temp = (wf_dict['main']['temp']) -273
        weather = wf_dict['weather'][0]['description']
        date_time = wf_dict['dt_txt']
        print "The weather for %s is %s and the temp is %.2f" % (date_time, weather, temp)
        i+=1

five_Forecast()
