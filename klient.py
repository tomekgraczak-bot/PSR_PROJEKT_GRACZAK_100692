import socket

polaczenie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
polaczenie.connect(("127.0.0.1", 8001))
print("polaczono z magazynem")

print("Dostepne komendy:")
print("stan")
print("kup klawiatura")
print("kup mysz")
print("kup monitor")
print("dostawa klawiatura")
print("dostawa mysz")
print("dostawa monitor")
print("koniec")

while True:
    komenda = input("Komenda: ")
    if komenda == "koniec":
        break
    polaczenie.sendall(komenda.encode())

polaczenie.close()