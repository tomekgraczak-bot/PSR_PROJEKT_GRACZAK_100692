import socket
import getpass

polaczenie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
polaczenie.connect(("127.0.0.1", 8001))
print("polaczono z magazynem")

print("Dostepne komendy:")
print("login")
print("wyloguj")
print("stan")
print("kup klawiatura (tylko klient)")
print("kup mysz (tylko klient)")
print("kup monitor (tylko klient)")
print("zamow klawiatura (tylko admin)")
print("zamow mysz (tylko admin)")
print("zamow monitor (tylko admin)")
print("koniec")

while True:
    komenda = input("Komenda: ")
    if komenda == "koniec":
        break
    if komenda == "login":
        login = input("Login: ")
        polaczenie.sendall(login.encode())
        haslo = getpass.getpass("Haslo: ")
        polaczenie.sendall(haslo.encode())
    if komenda != "login":
        polaczenie.sendall(komenda.encode())
    odpowiedz = polaczenie.recv(1024)
    print(odpowiedz.decode(), end="")

polaczenie.close()