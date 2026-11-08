
import socket

konto = 100
konto_magazyn = 0

klawiatury = 5
myszki = 10
monitory = 2

cena_klawiatury = 20
cena_myszy = 10
cena_monitora = 50

dostawa_inpost = 10
dostawa_dpd = 15

sprzedane = 0
sprzedane_klawiatury = 0
sprzedane_myszki = 0
sprzedane_monitory = 0

serwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serwer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serwer.bind(("127.0.0.1", 8001))
serwer.listen()

print("Magazyn czeka na polaczenie")

while True:
    polaczenie, adres = serwer.accept()
    print("Polaczono:", adres)

    rola = ""

    while True:
        dane = polaczenie.recv(4096)

        if not dane:
            break

        komenda = dane.decode()

        # LOGOWANIE USER
        if komenda == "user":
            rola = "user"
            polaczenie.sendall("Zalogowano jako user".encode())

        # LOGOWANIE ADMIN
        if komenda == "admin":
            rola = "admin"
            polaczenie.sendall("Zalogowano jako admin".encode())

        # WYLOGOWANIE
        if komenda == "wyloguj":
            rola = ""
            polaczenie.sendall("Wylogowano".encode())

        # STAN MAGAZYNU
        if komenda == "stan":
            tekst = (
                "Klawiatury: " + str(klawiatury) +
                "\nMyszki: " + str(myszki) +
                "\nMonitory: " + str(monitory) +
                "\nKonto klienta: " + str(konto) +
                "\nKonto magazynu: " + str(konto_magazyn) +
                "\nSprzedane razem: " + str(sprzedane) +
                "\nSprzedane klawiatury: " + str(sprzedane_klawiatury) +
                "\nSprzedane myszki: " + str(sprzedane_myszki) +
                "\nSprzedane monitory: " + str(sprzedane_monitory) +
                "\nZysk z marzy: " +
                str(sprzedane_klawiatury * cena_klawiatury * 10 // 100 +
                    sprzedane_myszki * cena_myszy * 10 // 100 +
                    sprzedane_monitory * cena_monitora * 10 // 100)
            )
            polaczenie.sendall(tekst.encode())

        # RAPORT CSV
        if komenda == "csv":
            if rola == "admin":
                tekst = (
                    "Produkt;Ilosc;Cena;Sprzedane;Zysk\n"
                    "Klawiatura;" + str(klawiatury) + ";" +
                    str(cena_klawiatury) + ";" +
                    str(sprzedane_klawiatury) + ";" +
                    str(sprzedane_klawiatury * cena_klawiatury * 10 // 100) + "\n"
                    "Mysz;" + str(myszki) + ";" +
                    str(cena_myszy) + ";" +
                    str(sprzedane_myszki) + ";" +
                    str(sprzedane_myszki * cena_myszy * 10 // 100) + "\n"
                    "Monitor;" + str(monitory) + ";" +
                    str(cena_monitora) + ";" +
                    str(sprzedane_monitory) + ";" +
                    str(sprzedane_monitory * cena_monitora * 10 // 100) + "\n"
                    "RAZEM;;;" + str(sprzedane) + ";" +
                    str(sprzedane_klawiatury * cena_klawiatury * 10 // 100 +
                        sprzedane_myszki * cena_myszy * 10 // 100 +
                        sprzedane_monitory * cena_monitora * 10 // 100)
                )
                polaczenie.sendall(tekst.encode())

            if rola != "admin":
                polaczenie.sendall("Brak dostepu".encode())

        # ZAKUP KLAWIATURY
        if komenda == "kup klawiatura":
            if rola != "user":
                polaczenie.sendall("Tylko user moze kupowac".encode())

            if rola == "user":
                polaczenie.sendall("Wybierz inpost lub dpd".encode())
                dostawa = polaczenie.recv(1024).decode()

                if dostawa == "inpost":
                    if klawiatury > 0 and konto >= cena_klawiatury + cena_klawiatury * 10 // 100 + dostawa_inpost:
                        klawiatury = klawiatury - 1
                        konto = konto - cena_klawiatury - cena_klawiatury * 10 // 100 - dostawa_inpost
                        konto_magazyn = konto_magazyn + cena_klawiatury + cena_klawiatury * 10 // 100
                        sprzedane = sprzedane + 1
                        sprzedane_klawiatury = sprzedane_klawiatury + 1
                        polaczenie.sendall("Kupiono klawiature (InPost)".encode())

                    else:
                        polaczenie.sendall("Brak towaru lub pieniedzy".encode())

                if dostawa == "dpd":
                    if klawiatury > 0 and konto >= cena_klawiatury + cena_klawiatury * 10 // 100 + dostawa_dpd:
                        klawiatury = klawiatury - 1
                        konto = konto - cena_klawiatury - cena_klawiatury * 10 // 100 - dostawa_dpd
                        konto_magazyn = konto_magazyn + cena_klawiatury + cena_klawiatury * 10 // 100
                        sprzedane = sprzedane + 1
                        sprzedane_klawiatury = sprzedane_klawiatury + 1
                        polaczenie.sendall("Kupiono klawiature (DPD)".encode())

                    else:
                        polaczenie.sendall("Brak towaru lub pieniedzy".encode())

                if dostawa != "inpost" and dostawa != "dpd":
                    polaczenie.sendall("Nieznana dostawa".encode())

        # ZAKUP MYSZY
        if komenda == "kup mysz":
            if rola != "user":
                polaczenie.sendall("Tylko user moze kupowac".encode())

            if rola == "user":
                polaczenie.sendall("Wybierz inpost lub dpd".encode())
                dostawa = polaczenie.recv(1024).decode()

                if dostawa == "inpost":
                    if myszki > 0 and konto >= cena_myszy + cena_myszy * 10 // 100 + dostawa_inpost:
                        myszki = myszki - 1
                        konto = konto - cena_myszy - cena_myszy * 10 // 100 - dostawa_inpost
                        konto_magazyn = konto_magazyn + cena_myszy + cena_myszy * 10 // 100
                        sprzedane = sprzedane + 1
                        sprzedane_myszki = sprzedane_myszki + 1
                        polaczenie.sendall("Kupiono mysz (InPost)".encode())

                    else:
                        polaczenie.sendall("Brak towaru lub pieniedzy".encode())

                if dostawa == "dpd":
                    if myszki > 0 and konto >= cena_myszy + cena_myszy * 10 // 100 + dostawa_dpd:
                        myszki = myszki - 1
                        konto = konto - cena_myszy - cena_myszy * 10 // 100 - dostawa_dpd
                        konto_magazyn = konto_magazyn + cena_myszy + cena_myszy * 10 // 100
                        sprzedane = sprzedane + 1
                        sprzedane_myszki = sprzedane_myszki + 1
                        polaczenie.sendall("Kupiono mysz (DPD)".encode())

                    else:
                        polaczenie.sendall("Brak towaru lub pieniedzy".encode())

                if dostawa != "inpost" and dostawa != "dpd":
                    polaczenie.sendall("Nieznana dostawa".encode())

        # ZAKUP MONITORA
        if komenda == "kup monitor":
            if rola != "user":
                polaczenie.sendall("Tylko user moze kupowac".encode())

            if rola == "user":
                polaczenie.sendall("Wybierz inpost lub dpd".encode())
                dostawa = polaczenie.recv(1024).decode()

                if dostawa == "inpost":
                    if monitory > 0 and konto >= cena_monitora + cena_monitora * 10 // 100 + dostawa_inpost:
                        monitory = monitory - 1
                        konto = konto - cena_monitora - cena_monitora * 10 // 100 - dostawa_inpost
                        konto_magazyn = konto_magazyn + cena_monitora + cena_monitora * 10 // 100
                        sprzedane = sprzedane + 1
                        sprzedane_monitory = sprzedane_monitory + 1
                        polaczenie.sendall("Kupiono monitor (InPost)".encode())

                    else:
                        polaczenie.sendall("Brak towaru lub pieniedzy".encode())

                if dostawa == "dpd":
                    if monitory > 0 and konto >= cena_monitora + cena_monitora * 10 // 100 + dostawa_dpd:
                        monitory = monitory - 1
                        konto = konto - cena_monitora - cena_monitora * 10 // 100 - dostawa_dpd
                        konto_magazyn = konto_magazyn + cena_monitora + cena_monitora * 10 // 100
                        sprzedane = sprzedane + 1
                        sprzedane_monitory = sprzedane_monitory + 1
                        polaczenie.sendall("Kupiono monitor (DPD)".encode())

                    else:
                        polaczenie.sendall("Brak towaru lub pieniedzy".encode())

                if dostawa != "inpost" and dostawa != "dpd":
                    polaczenie.sendall("Nieznana dostawa".encode())

        # ZAMOWIENIE KLAWIATURY DO MAGAZYNU
        if komenda == "zamow klawiatura":
            if rola != "admin":
                polaczenie.sendall("Tylko admin moze zamawiac".encode())

            if rola == "admin":
                polaczenie.sendall("Wybierz inpost lub dpd".encode())
                dostawa = polaczenie.recv(1024).decode()

                if dostawa == "inpost":
                    if konto_magazyn >= cena_klawiatury + dostawa_inpost:
                        klawiatury = klawiatury + 1
                        konto_magazyn = konto_magazyn - cena_klawiatury - dostawa_inpost
                        polaczenie.sendall("Dodano klawiature (InPost)".encode())

                    else:
                        polaczenie.sendall("Brak pieniedzy magazynu".encode())

                if dostawa == "dpd":
                    if konto_magazyn >= cena_klawiatury + dostawa_dpd:
                        klawiatury = klawiatury + 1
                        konto_magazyn = konto_magazyn - cena_klawiatury - dostawa_dpd
                        polaczenie.sendall("Dodano klawiature (DPD)".encode())

                    else:
                        polaczenie.sendall("Brak pieniedzy magazynu".encode())

                if dostawa != "inpost" and dostawa != "dpd":
                    polaczenie.sendall("Nieznana dostawa".encode())

        # ZAMOWIENIE MYSZY DO MAGAZYNU
        if komenda == "zamow mysz":
            if rola != "admin":
                polaczenie.sendall("Tylko admin moze zamawiac".encode())

            if rola == "admin":
                polaczenie.sendall("Wybierz inpost lub dpd".encode())
                dostawa = polaczenie.recv(1024).decode()

                if dostawa == "inpost":
                    if konto_magazyn >= cena_myszy + dostawa_inpost:
                        myszki = myszki + 1
                        konto_magazyn = konto_magazyn - cena_myszy - dostawa_inpost
                        polaczenie.sendall("Dodano mysz (InPost)".encode())

                    else:
                        polaczenie.sendall("Brak pieniedzy magazynu".encode())

                if dostawa == "dpd":
                    if konto_magazyn >= cena_myszy + dostawa_dpd:
                        myszki = myszki + 1
                        konto_magazyn = konto_magazyn - cena_myszy - dostawa_dpd
                        polaczenie.sendall("Dodano mysz (DPD)".encode())

                    else:
                        polaczenie.sendall("Brak pieniedzy magazynu".encode())

                if dostawa != "inpost" and dostawa != "dpd":
                    polaczenie.sendall("Nieznana dostawa".encode())

        # ZAMOWIENIE MONITORA DO MAGAZYNU
        if komenda == "zamow monitor":
            if rola != "admin":
                polaczenie.sendall("Tylko admin moze zamawiac".encode())

            if rola == "admin":
                polaczenie.sendall("Wybierz inpost lub dpd".encode())
                dostawa = polaczenie.recv(1024).decode()

                if dostawa == "inpost":
                    if konto_magazyn >= cena_monitora + dostawa_inpost:
                        monitory = monitory + 1
                        konto_magazyn = konto_magazyn - cena_monitora - dostawa_inpost
                        polaczenie.sendall("Dodano monitor (InPost)".encode())

                    else:
                        polaczenie.sendall("Brak pieniedzy magazynu".encode())

                if dostawa == "dpd":
                    if konto_magazyn >= cena_monitora + dostawa_dpd:
                        monitory = monitory + 1
                        konto_magazyn = konto_magazyn - cena_monitora - dostawa_dpd
                        polaczenie.sendall("Dodano monitor (DPD)".encode())

                    else:
                        polaczenie.sendall("Brak pieniedzy magazynu".encode())

                if dostawa != "inpost" and dostawa != "dpd":
                    polaczenie.sendall("Nieznana dostawa".encode())

    polaczenie.close()
    print("Klient rozlaczony")
