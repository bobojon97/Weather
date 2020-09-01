import pyowm

owm = pyowm.OWM('babbb8bb07c8f901a3e17f6337ca300a', {'language': 'ru'})

place = input('В каком городе/стране ?: ')

wer = owm.weather_manager().weather_at_place(place)
w = wer.get_weather()

temp = w.get_temperature('celsius')['temp']

print ('В городе ' , place , 'сейчас', w.get_detailed_status())

print ('Температура сейчас в районе ',str(temp))

if temp < 10:
	print('Сейчас  холодно одевайся два куртка  !')


elif temp < 20:
	print('Сейчас холодно, оденься потеплее')
	

else:
	print('Температура норм, одевайся что  угодно')
