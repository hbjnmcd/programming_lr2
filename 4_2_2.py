import requests
from bs4 import BeautifulSoup

def check_weather(city):

    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.771 YaBrowser/23.11.2.771 Yowser/2.5 Safari/537.36"
    }

    responce = requests.get(f"https://www.google.com/search?q=погода+в+{city}", headers=headers)

    soup = BeautifulSoup(responce.text, "html.parser")

    temperature = soup.select("#wob_tm")[0].getText()
    title = soup.select("#wob_dc")[0].getText()
    humidity = soup.select("#wob_hm")[0].getText()
    time = soup.select("#wob_dts")[0].getText()
    wind = soup.select("#wob_ws")[0].getText()

    print(time)
    print(title)
    print(f"Температура: {temperature}F")
    print(f"Влажность: {humidity}")
    print(f"Ветер: {wind}")

if __name__ == "__main__":
    city = str(input("Город: "))
    check_weather(city=city)
