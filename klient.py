import requests

odpowiedz = requests.get("http://127.0.0.1:8001/stan")
stan = odpowiedz.json()

print("Stan magazynu:")
for nazwa in stan:
    print(nazwa, stan[nazwa])