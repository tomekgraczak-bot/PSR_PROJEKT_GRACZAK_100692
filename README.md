# Rozproszone transakcje w sklepie internetowym

Projekt z Programowania systemów rozproszonych (temat 9), Tomasz Graczak, grupa 1EZ11.

System zamówień sklepu internetowego składa się z trzech niezależnych usług, każda z własną bazą danych:
- zamówienia (koordynator transakcji),
- magazyn,
- płatności.

Złożenie zamówienia jest transakcją rozproszoną: rezerwacja towaru i obciążenie konta muszą zostać zatwierdzone razem albo razem wycofane (protokół dwufazowy, 2PC). Projekt pokazuje też zachowanie systemu przy błędach: brak towaru i brak środków.

Stos: Python, FastAPI, SQLite.

## Stan prac
- [ ] magazyn
- [ ] płatności
- [ ] koordynator zamówień
- [ ] klient i scenariusze błędów
