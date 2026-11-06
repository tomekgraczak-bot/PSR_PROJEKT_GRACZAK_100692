# Sklep z rozproszonymi transakcjami

Projekt semestralny z Programowania systemów rozproszonych (temat 9).
Tomasz Graczak, grupa 1EZ11.

## Założenia
System sklepu internetowego złożony z trzech niezależnych usług, każda z własną bazą SQLite:
magazyn, płatności i koordynator zamówień.

Zamówienie to transakcja rozproszona: rezerwacja towaru i obciążenie konta muszą się udać razem albo wcale.
Zapewnia to protokół zatwierdzania dwufazowego (2PC): koordynator najpierw pyta obie usługi, czy mogą wykonać swoją część,
a potem zatwierdza albo wycofuje zmiany w obu.

System obsłuży sytuacje błędne: brak towaru, brak środków, niedostępną usługę oraz awarię koordynatora z odzyskaniem stanu.

## Etapy
1. Serwer magazynu i klient ✅
2. Usługa płatności
3. Koordynator i protokół 2PC
4. Scenariusze błędów i odzyskiwanie po awarii
5. Bazy SQLite, testy i pomiary

## Stan obecny (etap 1)
Pierwszy krok: serwer magazynu na gniazdach TCP i klient tekstowy.
Obsługuje stan, kupno (sprawdza towar i saldo konta) oraz dostawę.
Transakcja rozproszona zostanie dodana w kolejnych etapach.

## Uruchomienie
`py magazyn.py`, a w drugim terminalu `py klient.py`