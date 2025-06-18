**Notatka o wzbogaconych drzewach AVL**
W klasycznym drzewie AVL każdy węzeł przechowuje klucz, wskaźniki na poddrzewa, wysokość oraz balans drzewa. W drzewach wzbogaconych (ang. *augmented AVL*) dodajemy dodatkowe informacje do każdego węzła, aby wspierać nowe operacje w czasie O(log n). Poniżej omówienie czterech kluczowych funkcji:

---

## 1. `find_by_idx(idx)`

**Cel:** Zwraca wartość klucza znajdującego się na pozycji `idx` w porządku in-order (1-based).

**Dane dodatkowe:**

* Każdy węzeł przechowuje `size` = rozmiar poddrzewa (liczba węzłów w tym poddrzewie).

**Algorytm:**

1. Dla bieżącego węzła obliczamy `left_size = size(left)`.
2. Jeśli `idx == left_size + 1`, to bieżący węzeł jest szukanym (zwracamy `node.key`).
3. Jeśli `idx ≤ left_size`, schodzimy do lewego poddrzewa (`find_by_idx(left, idx)`).
4. W przeciwnym razie: przechodzimy do prawego poddrzewa, ale szukamy już pozycji `idx − (left_size + 1)`.

**Złożoność:** O(h) = O(log n), bo na każdym poziomie “przeskakujemy” do jednego z dzieci.

---

## 2. `sum_of_even()`

**Cel:** Oblicza sumę kluczy znajdujących się na parzystych pozycjach in-order.

**Dane dodatkowe:**

* Każdy węzeł przechowuje dwie wartości:

  * `sum_even` = suma kluczy w jego poddrzewie, które znajdują się na parzystych pozycjach globalnego in-order,
  * `sum_odd`  = suma kluczy na nieparzystych pozycjach.

**Utrzymanie:**

* Po każdej modyfikacji (wstawienie, usunięcie, rotacja) od dołu ku górze wywołujemy `recalc()`, które:

  1. Przelicza `height` i `size`.
  2. Pobiera od lewego i prawego dziecka ich parzyste i nieparzyste sumy.
  3. Ustala, czy bieżący węzeł ma w drzewie lokalnie parzysty czy nieparzysty indeks (to zależy od `size(left)`):

     * jeśli `(size(left)+1)` jest parzyste → dodaje swój klucz do `sum_even`, a sumy dzieci odpowiednio zamienia;
     * jeśli nieparzyste → dodaje swój klucz do `sum_odd`.

**Zwracanie:**

* Po prostu zwracamy `root.sum_even` (lub 0 dla pustego drzewa).

**Poprawność:**

* Dzięki dokładnemu przekazywaniu z każdego poddrzewa, które elementy są parzyste/nieparzyste, sumy zawsze odzwierciedlają aktualny układ in-order całego drzewa.

---

## 3. `insert_by_idx(idx, key)`

**Cel:** Wstawić nowy klucz tak, aby trafił na pozycję `idx` w porządku in-order, przesuwając wszystkie dotychczasowe elementy z tej i wyższych pozycji o jeden w prawo.

**Algorytm:**

1. Sprawdzamy, czy `1 ≤ idx ≤ size(root)+1`.
2. Rekurencyjnie schodzimy:

   * Jeśli `idx ≤ size(left)+1`, idziemy w lewo, wstawiając na tę pozycję;
   * W przeciwnym razie – do prawego poddrzewa z `idx’ = idx − (size(left)+1)`.
3. Na ścieżce powrotnej od wstawienia aktualizujemy wszystkie `size`, `height`, `sum_even`, `sum_odd` przez `recalc()`, a następnie wywołujemy `_rebalance()`.

**Poprawność:**

* Struktura in-order po wstawieniu to wstawienie elementu w właściwym “miejsce”.
* Przez aktualizację rozmiarów każde poddrzewo “wie”, jak zmienił się układ indeksów.
* Operacje rotacji zachowują porządek porównawczy i ponownie korygują wielkości/sumy, dzięki czemu AVL-owe własności są utrzymane.

---

## 4. `delete_by_idx(idx)`

**Cel:** Usunąć element z porządkiem in-order na pozycji `idx`.

**Algorytm:**

1. Sprawdzamy, czy `1 ≤ idx ≤ size(root)`.
2. Rekurencyjnie schodzimy:

   * Gdy `idx == size(left)+1`, to to jest węzeł do usunięcia.

     * Jeśli ma ≤ 1 dziecka – zwracamy to dziecko (lub `None`).
     * Jeśli ma 2 dzieci – szukamy jego kolejnego elementu (`succ` – najmniejszy w prawym poddrzewie), kopiujemy `succ.key` do bieżącego węzła i rekurencyjnie usuwamy `succ` z prawego poddrzewa (tam zawsze będzie na indeksie 1).
   * Jeśli `idx ≤ size(left)`, schodzimy w lewo; w przeciwnym razie – w prawo z indeksem zmienionym o `left_size+1`.
3. Po usunięciu od strony liścia w górę: `recalc()` + `_rebalance()`.

**Poprawność:**

* In-order bez usuniętego elementu → poprawny wynik.
* Dzięki zmianie `size` i sum po każdej zmianie i ponownym zbalansowaniu, całe drzewo spełnia invariants AVL i invariants sum/parzystości indeksów.

---

### Złożoności wszystkich operacji

* **Wysokość drzewa:** O(log n)
* **Find\_by\_idx, insert\_by\_idx, delete\_by\_idx:** każde schodzi i cofa się ścieżką drzewa, wykonując stałą liczbę obliczeń i ewentualnie rotację → **O(log n)**
* **sum\_of\_even / sum\_of\_odd:** O(1) (odczyt z korzenia)

Dzięki przechowywaniu węzłów dodatkowych informacji (*size*, *sum\_even*, *sum\_odd*) i utrzymywaniu ich w czasie obrotów, uzyskujemy bardzo wydajne operacje indeksowane oraz szybki dostęp do agregatów wartości.
