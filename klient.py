
import socket

klient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klient.connect(("127.0.0.1", 8001))

print("Polaczono z magazynem")

while True:
    rola = input("Kim jestes? (user/admin): ")

    if rola == "user" or rola == "admin":
        klient.sendall(rola.encode())
        print(klient.recv(4096).decode())

        if rola == "user":
            print("Komendy:\nstan\nkup klawiatura\nkup mysz\nkup monitor\nwyloguj\nkoniec")

        if rola == "admin":
            print("Komendy:\nstan\nzamow klawiatura\nzamow mysz\nzamow monitor\nwyloguj\nkoniec")

        while True:
            komenda = input("Komenda: ")

            if komenda == "koniec":
                klient.close()
                quit()

            if komenda == "wyloguj":
                klient.sendall("wyloguj".encode())
                print(klient.recv(4096).decode())
                break

            if komenda == "stan":
                klient.sendall("stan".encode())
                print(klient.recv(4096).decode())

                if rola == "admin":
                    klient.sendall("csv".encode())
                    print(klient.recv(4096).decode())

            if komenda == "kup klawiatura" or komenda == "kup mysz" or komenda == "kup monitor":
                if rola == "user":
                    klient.sendall(komenda.encode())
                    print(klient.recv(4096).decode())

                    dostawa = input("> ")
                    klient.sendall(dostawa.encode())
                    print(klient.recv(4096).decode())

                if rola != "user":
                    print("Tylko user moze kupowac")

            if komenda == "zamow klawiatura" or komenda == "zamow mysz" or komenda == "zamow monitor":
                if rola == "admin":
                    klient.sendall(komenda.encode())
                    print(klient.recv(4096).decode())

                    dostawa = input("> ")
                    klient.sendall(dostawa.encode())
                    print(klient.recv(4096).decode())

                if rola != "admin":
                    print("Tylko admin moze zamawiac")

    else:
        print("Nieznany uzytkownik")
