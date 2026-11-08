import socket
import hashlib

konto = 100
konto_magazyn = 0

klawiatury = 5
myszki = 10
monitory = 2

cena_klawiatury = 20
cena_myszy = 10
cena_monitora = 50

cena_inpost = 10
cena_dpd = 15

hash_user = "6ad14ba9986e3615423dfca256d04e3f"
hash_admin = "0192023a7bbd73250516f069df18b500"

serwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serwer.bind(("127.0.0.1", 8001))
serwer.listen()
print("magazyn czeka na polaczenie")

while True:
    polaczenie, adres = serwer.accept()
    plik = polaczenie.makefile("w")
    zalogowany = ""
    krok = ""
    while True:
        bajty = polaczenie.recv(1024)
        if not bajty:
            break
        komenda = bajty.decode()
        hash_komendy = hashlib.md5(bajty).hexdigest()

        if krok == "user":
            if hash_komendy == hash_user:
                zalogowany = "user"
                print("zalogowano: user", file=plik)
            if hash_komendy != hash_user:
                print("zle haslo", file=plik)
            krok = ""

        if krok == "admin":
            if hash_komendy == hash_admin:
                zalogowany = "admin"
                print("zalogowano: admin", file=plik)
            if hash_komendy != hash_admin:
                print("zle haslo", file=plik)
            krok = ""

        if krok == "klawiatura":
            cena_wysylki = 0
            if komenda == "inpost":
                cena_wysylki = cena_inpost
            if komenda == "dpd":
                cena_wysylki = cena_dpd
            if cena_wysylki == 0:
                print("nie ma takiej dostawy", file=plik)
            if cena_wysylki > 0:
                if klawiatury == 0:
                    print("brak klawiatur", file=plik)
                if klawiatury > 0:
                    if konto < cena_klawiatury + cena_wysylki:
                        print("za malo pieniedzy", file=plik)
                    if konto >= cena_klawiatury + cena_wysylki:
                        klawiatury = klawiatury - 1
                        konto = konto - cena_klawiatury - cena_wysylki
                        konto_magazyn = konto_magazyn + cena_klawiatury
                        print("kupiono klawiature, dostawa:", komenda, "zostalo:", klawiatury, "stan konta:", konto, file=plik)
            krok = ""

        if krok == "mysz":
            cena_wysylki = 0
            if komenda == "inpost":
                cena_wysylki = cena_inpost
            if komenda == "dpd":
                cena_wysylki = cena_dpd
            if cena_wysylki == 0:
                print("nie ma takiej dostawy", file=plik)
            if cena_wysylki > 0:
                if myszki == 0:
                    print("brak myszek", file=plik)
                if myszki > 0:
                    if konto < cena_myszy + cena_wysylki:
                        print("za malo pieniedzy", file=plik)
                    if konto >= cena_myszy + cena_wysylki:
                        myszki = myszki - 1
                        konto = konto - cena_myszy - cena_wysylki
                        konto_magazyn = konto_magazyn + cena_myszy
                        print("kupiono mysz, dostawa:", komenda, "zostalo:", myszki, "stan konta:", konto, file=plik)
            krok = ""

        if krok == "monitor":
            cena_wysylki = 0
            if komenda == "inpost":
                cena_wysylki = cena_inpost
            if komenda == "dpd":
                cena_wysylki = cena_dpd
            if cena_wysylki == 0:
                print("nie ma takiej dostawy", file=plik)
            if cena_wysylki > 0:
                if monitory == 0:
                    print("brak monitorow", file=plik)
                if monitory > 0:
                    if konto < cena_monitora + cena_wysylki:
                        print("za malo pieniedzy", file=plik)
                    if konto >= cena_monitora + cena_wysylki:
                        monitory = monitory - 1
                        konto = konto - cena_monitora - cena_wysylki
                        konto_magazyn = konto_magazyn + cena_monitora
                        print("kupiono monitor, dostawa:", komenda, "zostalo:", monitory, "stan konta:", konto, file=plik)
            krok = ""

        if komenda == "user":
            krok = "user"

        if komenda == "admin":
            krok = "admin"

        if komenda == "wyloguj":
            print("wylogowano:", zalogowany, file=plik)
            zalogowany = ""

        if komenda == "kup klawiatura":
            if zalogowany != "user":
                print("kupowac moze tylko zalogowany klient", file=plik)
            if zalogowany == "user":
                print("wybierz dostawe: inpost", cena_inpost, "zl albo dpd", cena_dpd, "zl", file=plik)
                krok = "klawiatura"

        if komenda == "kup mysz":
            if zalogowany != "user":
                print("kupowac moze tylko zalogowany klient", file=plik)
            if zalogowany == "user":
                print("wybierz dostawe: inpost", cena_inpost, "zl albo dpd", cena_dpd, "zl", file=plik)
                krok = "mysz"

        if komenda == "kup monitor":
            if zalogowany != "user":
                print("kupowac moze tylko zalogowany klient", file=plik)
            if zalogowany == "user":
                print("wybierz dostawe: inpost", cena_inpost, "zl albo dpd", cena_dpd, "zl", file=plik)
                krok = "monitor"

        if komenda == "zamow klawiatura":
            if zalogowany != "admin":
                print("tylko admin moze zamawiac towar", file=plik)
            if zalogowany == "admin":
                if konto_magazyn < cena_klawiatury:
                    print("magazyn nie ma pieniedzy na zamowienie", file=plik)
                if konto_magazyn >= cena_klawiatury:
                    klawiatury = klawiatury + 1
                    konto_magazyn = konto_magazyn - cena_klawiatury
                    print("przyjeto klawiature, jest:", klawiatury, "konto magazynu:", konto_magazyn, file=plik)

        if komenda == "zamow mysz":
            if zalogowany != "admin":
                print("tylko admin moze zamawiac towar", file=plik)
            if zalogowany == "admin":
                if konto_magazyn < cena_myszy:
                    print("magazyn nie ma pieniedzy na zamowienie", file=plik)
                if konto_magazyn >= cena_myszy:
                    myszki = myszki + 1
                    konto_magazyn = konto_magazyn - cena_myszy
                    print("przyjeto mysz, jest:", myszki, "konto magazynu:", konto_magazyn, file=plik)

        if komenda == "zamow monitor":
            if zalogowany != "admin":
                print("tylko admin moze zamawiac towar", file=plik)
            if zalogowany == "admin":
                if konto_magazyn < cena_monitora:
                    print("magazyn nie ma pieniedzy na zamowienie", file=plik)
                if konto_magazyn >= cena_monitora:
                    monitory = monitory + 1
                    konto_magazyn = konto_magazyn - cena_monitora
                    print("przyjeto monitor, jest:", monitory, "konto magazynu:", konto_magazyn, file=plik)

        if komenda == "stan":
            print("klawiatury:", klawiatury, "myszki:", myszki, "monitory:", monitory, file=plik)
            print("stan konta:", konto, file=plik)
            print("konto magazynu:", konto_magazyn, file=plik)
            print("zalogowany:", zalogowany, file=plik)
            print("dostawa: inpost", cena_inpost, "zl, dpd", cena_dpd, "zl", file=plik)

        plik.flush()
    polaczenie.close()