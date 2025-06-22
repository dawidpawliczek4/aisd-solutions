Poniżej znajdziesz szczegółowe wyjaśnienie algorytmu wykorzystującego dekompozycję centroidową, działającego w **O(n log n)**, krok po kroku.

---

## 1. Co to jest *centroid* drzewa?

* Centroidem drzewa nazywamy taki wierzchołek, którego usunięcie (razem ze wszystkimi incydentnymi krawędziami) rozdziela drzewo na poddrzewa o rozmiarze co najwyżej *n/2*.
* Kluczowa własność: w każdym drzewie istnieje jeden lub dwa centroidy, a znalezienie ich można zrobić w **O(n)** przez jedno przejście DFS liczące rozmiary poddrzew.

---

## 2. Idea dekompozycji centroidowej

1. **Wybieramy centroid** aktualnego drzewa (lub poddrzewa).
2. **Liczymy pary wierzchołków**, których najkrótsza ścieżka **przechodzi przez tego centroida** i ma sumę wag **= C**.
3. **„Wycinamy” centroid** z drzewa, uzyskując kilka mniejszych poddrzew (każde o rozmiarze ≤ n/2), i **rekurencyjnie** powtarzamy krok 1–3 na każdym z nich.

Dzięki temu każde wierzchołki i każda krawędź biorą udział w liczbie poziomów rekurencji **≤ O(log n)**.

---

## 3. Zliczanie par przez jeden centroid

Załóżmy, że *w* to nasz wybrany centroid. Chcemy policzyć wszystkie pary (u,v) takich, że najkrótsza ścieżka u–v **przechodzi przez w** i suma wag= C. Robimy tak:

1. **Mapa `freq`**: na początku mamy tylko ścieżkę długości 0 (punkt w samym wierzchołku w):

   ```
   freq = { 0 ↦ 1 }  
   ```
2. **Dla każdego poddrzewa** wycinanego po usunięciu w:

   * **Zbieramy** do listy `distances` odległości (suma wag) od w do wszystkich wierzchołków w tym poddrzewie, przez prosty DFS.
   * **Dla każdej** odległości d ∈ `distances` sprawdzamy, ile jest w `freq` odległości r takich, że

     ```
       r + d = C   ⇔   r = C − d
     ```

     i dokładamy do globalnego wyniku answer wartość `freq[C − d]`.
   * **Dopiero po** policzeniu tych par scalamy odległości z `distances` do `freq`, robiąc

     ```
       freq[d] += 1   dla każdego d ∈ distances
     ```

   Dzięki temu pary łączą zawsze odległość z już „udostępnionych” innych poddrzew z odległością z bieżącego.

Cały ten etap – zbieranie DFS + przegląd listy + aktualizacja mapy – kosztuje **O(size\_of\_this\_subtree)** na danym poziomie rekurencji.

---

## 4. Rekurencja na mniejszych poddrzewach

Po przetworzeniu centroida „usuwamy” go (oznaczamy jako przetworzony) i dla każdego fragmentu drzewa, które pozostało, **oddzielnie** powtarzamy całą procedurę. Ponieważ po każdym cięciu największe poddrzewo ma rozmiar ≤ n/2, głębokość rekurencji jest **O(log n)**.

---

## 5. Poprawność i brak wielokrotnego zliczania

* **Każda para** wierzchołków albo:

  1. leży całkowicie w jednym z poddrzew po usunięciu w — wtedy zostanie policzona w rekurencji na tym poddrzewie,
  2. albo jej ścieżka przechodzi przez w — wtedy zostaje policzona dokładnie raz w kroku 3.
* Dzięki temu **żaden przypadek nie ginie** i **nikt nie jest liczony dwukrotnie**.

---

## 6. Analiza złożoności

1. Na **każdym poziomie** dekompozycji przechodzimy DFS-em przez wszystkie wierzchołki i krawędzie danego (pod)drzewa — koszt O(n) rozłożony na sumę wszystkich poddrzew z tej warstwy.
2. Liczba **poziomów** ≤ O(log n), ponieważ każde cięcie co najmniej **połowę** wierzchołków przenosi do mniejszych rekurencji.
3. Operacje na haściówce/mapie (`freq`) przyjmuje się średnio za O(1) na wstawienie/odczyt.

Łącznie daje to **O(n log n)** czasu oraz **O(n)** dodatkowej pamięci (mapa `freq` osiąga łącznie rozmiar O(n) w danej warstwie, ale nie więcej).

---

🎯 **Podsumowanie**:

* *Centroid* gwarantuje, że każdy poziom dekompozycji kosztuje proporcjonalnie do liczby wierzchołków.
* *Liczba poziomów* jest ograniczona logarytmem z *n*.
* *Zliczanie* par odbywa się w każdej warstwie liniowo względem wielkości drzewa i jest dokładne oraz bez duplikatów.
