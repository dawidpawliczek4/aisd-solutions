## Hashowanie

oczekiwania liczba kolizji dla n elementow, wielkosc tablicy m=n^2
EX = $\binom{n}{k}$ * 1/(n^2)


$\binom{n}{k}$ - liczba par mogacych kolidowac
1/n^2 - ppb kolizji gdy h(x) jest 'dobre'

EX = (n^2 - n)/2 * 1/n^2 < 1/2 z Markova

## Słownik statyczny
Chcemy, aby suma po (nj)^2 < 4n, gdzie nj- liczba kluczy w j-tym kubelku.

Pamiec
Potrzebujemy (dla dobrze wylosowanej funkcji)
- Nie wiecej niz 4n komorek na tablice wtorne
- 3 komorki na zapameitanie funkcji pierwotnej
- na kazda tablice wtorna 3 komorki - jeden na rozmiar, dwa na parametry funkcji, w sumie 3n
