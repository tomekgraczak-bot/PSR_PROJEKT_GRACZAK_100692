# PSR - projekt semestralny

Projekt z Programowania systemów rozproszonych, temat 9 - rozproszone transakcje.
Tomasz Graczak, grupa 1EZ11

## O projekcie

Robię system zamówień dla sklepu internetowego. Będzie się składał z trzech osobnych usług: magazynu, płatności i zamówień. Każda usługa ma mieć swoją bazę danych w SQLite.

Gdy klient składa zamówienie, trzeba zrobić dwie rzeczy w dwóch różnych usługach: zarezerwować towar w magazynie i pobrać pieniądze z konta. Obie rzeczy muszą się udać razem. Jeśli jedna się nie uda, druga też ma zostać cofnięta. Do tego użyję protokołu dwufazowego (2PC). Usługa zamówień najpierw pyta magazyn i płatności, czy mogą wykonać swoją część, a dopiero potem zatwierdza albo wycofuje zmiany w obu.

Chcę też pokazać, co się dzieje przy błędach: gdy brakuje towaru, gdy na koncie jest za mało pieniędzy, gdy jedna z usług nie odpowiada i gdy usługa zamówień wyłączy się w trakcie transakcji.

## Plan

1. serwer magazynu i klient - zrobione
2. usługa płatności
3. usługa zamówień i protokół 2PC
4. obsługa błędów i odzyskiwanie po awarii
5. bazy SQLite, testy i pomiary czasu

## Co jest zrobione

Na razie zrobiłem pierwszy krok, czyli serwer magazynu na gniazdach TCP i prostego klienta. W kliencie wpisuje się komendy, a serwer wypisuje wynik. Można sprawdzić stan, kupić towar i przyjąć dostawę. Przy kupnie serwer sprawdza, czy towar jest na stanie i czy na koncie są pieniądze. Transakcje rozproszone będą w