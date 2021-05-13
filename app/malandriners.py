import requests


def web():
    return "https://insignias.malandriners.dev/"


def happiest():
    response = requests.get("https://insignias.malandriners.dev/insignias")
    lista_de_malandriners = response.json()
    happy_list = [(malandrin['usuario'], malandrin['humor']['grinning']) for malandrin in lista_de_malandriners]

    return max(happy_list, key=lambda x: x[1])

