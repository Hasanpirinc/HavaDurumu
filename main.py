import requests

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, "aa41652306df04226be0c704c31b3c07")
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "sıcaklık": round((data["main"]["temp"] - 273.15), 1),
            "nem": data["main"]["humidity"],
            "rüzgar hızı": data["wind"]["speed"],
            "gökyüzü durumu": data["weather"][0]["description"],
        }
        return weather
    else:
        return False


def main():
    city = "Trabzon"
    weather = get_weather(city)

    if weather:
        print("Şu anda {}'da hava durumu:\n\n".format(city))
        print("* Sıcaklık: {}°C".format(weather["sıcaklık"]))
        print("* Nem: {}%".format(weather["nem"]))
        print("* Rüzgar hızı: {} km/s".format(weather["rüzgar hızı"]))
        print("* Gökyüzü durumu: {}".format(weather["gökyüzü durumu"]))
    else:
        print("Hava durumu bilgisi alınamadı.")


if __name__ == "__main__":
    main()