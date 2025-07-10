import requests
import time

city_try = ["Киев", "Полтава", "Мариуполь", "Одесса", "Львов"]
city = input("Ведите город")

API = " API "

a = 15
d = 17
#Проверка
if city in city_try:
    print("Код 100")
else:
    while city not in city_try:
        city = input("В базе данных нет такого города воспользуйтесь те что есть ""Киев"", ""Полтава"", ""Мариуполь"", ""Одесса"", ""Львов"" ")

Try = ["дождь","небольшой дождь","легкий дождь","умеренный дождь","сильный дождь","проливной дождь","очень сильный дождь","ливень","ливневый дождь","гроза с дождём","гроза и дождь","дождь с грозой","моросящий дождь","морось","слабый дождь","местами дождь","временами дождь","периодический дождь","дождь с переходом в снег","мокрый дождь", "сильный ливень"]

#Задержка чекеро
while a < d:
    print("Код 101")
    time.sleep(10800)
    parametrs = {
        "q": city,
        "appid": API,
        "units": "metric",
        "lang": "ru"
    }
    parametrs1 = {
        "q": city,
        "appid": API,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parametrs)
    response1 = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parametrs1)
    data = response.json()
    data1 = response1.json()
    description_3h = data1["list"][0]["weather"][0]["description"]
    data = {
        "Температура": data["main"]["temp"],
        "Дождь": data["weather"][0]["description"]
    }
    if  description_3h.lower() in [x.lower() for x in Try]:

        print(data["Температура"], "Сейчас")
        print(data["Дождь"], "Сейчас")
        print(description_3h)
        requests.post("https://ntfy.sh/ СВОЙ СЮДА", data=description_3h.encode("utf-8"))

    else:
        print("Дождя через 3 часа не ожидается.")

