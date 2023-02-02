from pyowm import OWM


#  получение градуса
def weather(city):
    try:
        owm = OWM('a2a7b3437211865ada91e23f56c2c442')
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(city)
        w = observation.weather
        return f"Текущая температура в \"{city}\": {w.temperature('celsius')['temp']}°C"
    except:
        return 'город указан неверно!'
