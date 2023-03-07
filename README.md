Zadanie 4. Dokumenty
=================
Plik `identyfikator.txt` zawiera 200 wierszy. W każdym wierszu jest zapisany
identyfikator pewnego dokumentu, który składa się z serii (trzy wielkie litery alfabetu
łacińskiego) oraz sześciu cyfr.
Napisz program(-y), w wyniku działania którego(-ych) otrzymasz odpowiedzi do poniższych
zadań.

Uwaga: Plik `identyfikator_przyklad.txt` zawiera przykładowe dane (20 wierszy).
Odpowiedzi dla danych z tego pliku są podane pod treściami zadań.

Zadanie 4.1. (0–3)
=
Podaj identyfikatory (seria+numer) tych dokumentów z pliku `identyfikator.txt`,
których suma cyfr z numerycznej części jest największa. Odpowiedź zapisz w pliku
`wyniki4_1.txt`, po jednym identyfikatorze w wierszu, w kolejności zgodnej z kolejnością
w pliku identyfikator.txt. W pliku `identyfikator_przyklad.txt` jest jeden taki identyfikator. 

Prawidłowa odpowiedź dla pliku `identyfikator_przyklad.txt`:\
`CHY728985`

Zadanie 4.2. (0–4)
=
Podaj wszystkie te identyfikatory dokumentów z pliku `identyfikator.txt`, których seria
lub numer są palindromami, czyli czytane od lewej do prawej i od prawej do lewej są takie
same. Odpowiedź zapisz w pliku `wyniki4_2.txt`, po jednym identyfikatorze w wierszu,
w kolejności zgodnej z kolejnością w pliku `identyfikator.txt`. 

Prawidłowa odpowiedź dla pliku `identyfikator_przyklad.txt`:\
`KOK201272`\
`PIP417543`\
`MOS302203`

Zadanie 4.3. (0–4)
=
Poprawność identyfikatora dokumentu potwierdza pierwsza cyfra z jego numerycznej części,
która jest cyfrą kontrolną.\
Aby sprawdzić poprawność identyfikatora danego dokumentu, należy wartość każdego
elementu identyfikatora (poza cyfrą kontrolną) pomnożyć przez odpowiednią wagę. Wagi
poszczególnych składowych identyfikatora to kolejno: 7, 3, 1, 7, 3, 1, 7, 3. Otrzymane iloczyny
należy zsumować i policzyć resztę z dzielenia tej sumy przez 10 (mod 10). Jeśli uzyskana w ten
sposób liczba jest równa wartości pierwszej cyfry z identyfikatora dokumentu, to identyfikator
jest poprawny. 

Pierwsza cyfra z numerycznej części identyfikatora jest równa 4, zatem identyfikator
dokumentu jest poprawny.\
W pliku `identyfikator.txt` znajdują się identyfikatory, z których część jest poprawna,
a część – niepoprawna. Podaj wszystkie identyfikatory dokumentów z tego pliku, które są
niepoprawne. Odpowiedź zapisz w pliku `wyniki4_3.txt`, po jednym identyfikatorze
w wierszu, w kolejności zgodnej z kolejnością w pliku `identyfikator.txt`.
Prawidłowa odpowiedź dla pliku `identyfikator_przyklad.txt`:\
`NHO307984`\
`SEH422297`\
`MOS302203`

ODPOWIEDZI
=
4.1
=
Za pełną poprawną odpowiedź – **3 punkty**\
Za niepełna poprawną odpowiedź (podanie jednego z
dwóch identyfikatorów) – **2 punkty**\
Za podanie największej sumy (45) zamiast identyfikatorów
– **1 punkt**

Prawidłowa odpowiedź:\
**GYJ959787**\
**JOK786969**

4.2
=
Za prawidłową odpowiedź – **4 punkty**\
W przypadku pominięcia tylko jednego identyfikatora
z palindromem w „serii” (części literowej) – **3 punkty**\
Za podanie odpowiedzi zawierającej tylko identyfikatory
z palindromami w „serii” (części literowej) – czyli
pominięcia MBF340043 – **2 punkty**\
Za podanie w wyniku od 1 do 4 prawidłowych
identyfikatorów – **1 punkt**.

*Prawidłowa odpowiedź*:\
MBF340043\
JKJ452719\
GFG148345\
AXA231829\
KIK866983\
LOL695279

4.3
=
Za podanie pełnej prawidłowej odpowiedzi czyli wszystkich
7 „nieprawidłowych” (zgodnie z treścią zadania) numerów
identyfikacyjnych – **4 punkty**\
Za podanie 6 numerów identyfikacyjnych – **3 punkty**\
Za podanie 5 numerów identyfikacyjnych – **2 punkty**\
Za podanie od jednego do czterech numerów – **1 punkt**

Prawidłowa odpowiedź:\
LIK235378\
MBF340043\
HFG378931\
KIJ511146\
NUK840936\
OKH427482\
RTS278686
