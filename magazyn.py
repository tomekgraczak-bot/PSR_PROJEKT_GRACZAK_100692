import socket

konto = 100

klawiatury = 5
myszki = 10
monitory = 2

cena_klawiatury = 20
cena_myszy = 10
cena_monitora = 50

serwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serwer.bind(("127.0.0.1", 8001))
serwer.listen()
print("magazyn czeka na polaczenie")

while True:
    polaczenie, adres = serwer.accept()
    while True:
        bajty = polaczenie.recv(1024)
        if not bajty:
            break
        komenda = bajty.decode()

        if komenda == "kup klawiatura":
            if klawiatury == 0:
                print("brak klawiatur")
            if klawiatury > 0:
                if konto < cena_klawiatury:
                    print("za malo pieniedzy")
                if konto >= cena_klawiatury:
                    klawiatury = klawiatury - 1
                    konto = konto - cena_klawiatury
                    print("sprzedano klawiature, zostalo:", klawiatury)
            print("stan konta:", konto)

        if komenda == "kup mysz":
            if myszki == 0:
                print("brak myszek")
            if myszki > 0:
                if konto < cena_myszy:
                    print("za malo pieniedzy")
                if konto >= cena_myszy:
                    myszki = myszki - 1
                    konto = konto - cena_myszy
                    print("sprzedano mysz, zostalo:", myszki)
            print("stan konta:", konto)

        if komenda == "kup monitor":
            if monitory == 0:
                print("brak monitorow")
            if monitory > 0:
                if konto < cena_monitora:
                    print("za malo pieniedzy")
                if konto >= cena_monitora:
                    monitory = monitory - 1
                    konto = konto - cena_monitora
                    print("sprzedano monitor, zostalo:", monitory)
            print("stan konta:", konto)

        if komenda == "dostawa klawiatura":
            klawiatury = klawiatury + 1
            print("przyjeto klawiature, jest:", klawiatury)
            print("stan konta:", konto)

        if komenda == "dostawa mysz":
            myszki = myszki + 1
            print("przyjeto mysz, jest:", myszki)
            print("stan konta:", konto)

        if komenda == "dostawa monitor":
            monitory = monitory + 1
            print("przyjeto monitor, jest:", monitory)
            print("stan konta:", konto)

        if komenda == "stan":
            print("klawiatury:", klawiatury, "myszki:", myszki, "monitory:", monitory)
            print("stan konta:", konto)
    polaczenie.close()