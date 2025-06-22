### Zadanie B – Najkrótszy superciąg (SCS) dwóch ciągów

*(strukturę zachowuję: 1 intuicja, 2 pseudokod, 3 poprawność, 4 złożoność)*

---

#### 1. Intuicja

Jeśli dwie sekwencje **X** i **Y** mają długi **najdłuższy wspólny podciąg** (LCS), to właśnie ten wspólny rdzeń możemy wykorzystać, aby „zszyć” ciągi, dopisując tylko znaki, które nie pokrywają się w LCS.
Fakty:

* Minimalna długość SCS = `|X| + |Y| – |LCS(X,Y)|`.
* Sam superciąg otrzymujemy, **wędrując jednocześnie** po X i Y i wypisując znak, który akurat „wygrywa” (tzn. jeśli literki są równe – raz, jeśli różne – ten z wcześniejszym wyborem w tablicy LCS).

---

#### 2. Pseudokod

```text
procedure SCS(X[1..m], Y[1..n])
    // 1. klasyczne DP dla LCS
    allocate L[0..m][0..n]
    for i←0..m: L[i][0] ← 0
    for j←0..n: L[0][j] ← 0
    for i←1..m:
        for j←1..n:
            if X[i] = Y[j]:
                L[i][j] ← L[i-1][j-1] + 1
            else
                L[i][j] ← max(L[i-1][j], L[i][j-1])

    // 2. odtwarzanie superciągu (od końca)
    i←m; j←n; Z ← empty stack
    while i>0 or j>0:
        if i>0 and j>0 and X[i] = Y[j]:
            push(Z, X[i]);        i←i-1; j←j-1
        else if j=0 or (i>0 and L[i-1][j] ≥ L[i][j-1]):
            push(Z, X[i]);        i←i-1
        else:
            push(Z, Y[j]);        j←j-1

    return reverse(Z)            // gotowy najkrótszy superciąg
```

---

#### 3. Poprawność

Indukcja po długości prefiksów w macierzy `L` daje poprawność tablicy LCS – klasyczny wynik.
Rekonstrukcja:

* **Równy znak**: gdy `X[i]=Y[j]`, najlepiej wziąć go raz – i długość LCS obniża się o 1, więc tą ścieżką odnajdujemy optymalne skrzyżowanie.
* **Różne znaki**: wybieramy gałąź, która pozostawia większy LCS – dzięki temu gwarantujemy, że w dalszej części ciągle istnieje wspólny podciąg o wymaganej długości.

Dopisywanie „nadmiarowych” znaków dokładnie tych, które nie leżą w LCS, prowadzi do łańcucha o długości `m+n−|LCS|`; lemat długości wyklucza istnienie krótszego superciągu, więc algorytm zwraca optymalny wynik. ∎

---

#### 4. Złożoność

* **Czas**: wypełnianie tablicy `L` – `Θ(m·n)`; odtworzenie wyniku – `O(m+n)`.
* **Pamięć**: `Θ(m·n)` (da się zredukować do `O(min(m,n))` dla samej długości, a następnie wykonać back-tracking fragmentami).

---

## Rozszerzenie – najkrótszy superciąg **trzech** ciągów X, Y, Z

---

### 1. Intuicja

Dla trzech sekwencji problem nie redukuje się już do różnicy z LCS; potrzebny jest pełny dynamic-programming w **3 wymiarach**:
`DP[i][j][k]` = minimalna długość SCS trójek prefiksów `X1..i`, `Y1..j`, `Z1..k`.
Rekurencja:

* Jeśli ostatnie znaki jednakowe (`xi = yj = zk`), możemy dopisać je **raz**:
  `DP[i][j][k] = 1 + DP[i-1][j-1][k-1]`.
* W przeciwnym razie próbujemy usunąć ostatni znak z jednego z ciągów i wybieramy minimum:

  ```
  DP[i][j][k] = 1 + min( DP[i-1][j][k],
                         DP[i][j-1][k],
                         DP[i][j][k-1] )
  ```

  (bo zawsze któryś znak musimy wypisać, zmniejszając jeden z indeksów).

Po obliczeniu DP wystarczy znów cofnąć się po macierzy (3D-backtracking), aby zrekonstruować sam superciąg.

---

### 2. Pseudokod

```
procedure SCS3(X[1..m], Y[1..n], Z[1..p])
    allocate D[0..m][0..n][0..p]

    // 1) inicjalizacje brzegowe
    for i←0..m: for j←0..n: D[i][j][0] ← i+j
    for i←0..m: for k←0..p: D[i][0][k] ← i+k
    for j←0..n: for k←0..p: D[0][j][k] ← j+k

    // 2) wypełnianie
    for i←1..m:
        for j←1..n:
            for k←1..p:
                if X[i]=Y[j]=Z[k]:
                    D[i][j][k] ← 1 + D[i-1][j-1][k-1]
                else:
                    D[i][j][k] ← 1 + min(D[i-1][j][k],
                                          D[i][j-1][k],
                                          D[i][j][k-1])

    // 3) back-tracking: identyczny duch jak dla 2D, pomijam szczegóły
    return BUILD_STRING_FROM(D, X, Y, Z)
```

`BUILD_STRING_FROM` przechodzi od `(m,n,p)` w dół, zawsze cofając się w kierunku komórki, która została wybrana w minimum (lub w przypadku trzech równych liter – cofając się po przekątnej i zapisując literę tylko raz).

---

### 3. Poprawność

Indukcja po sumie indeksów `(i+j+k)` dowodzi, że każda komórka `D[i][j][k]` jest minimalną możliwą długością superciągu trzech prefiksów:

* **Równe litery**: znak występuje w każdym ciągu, więc musi wystąpić co najmniej raz w SCS – wstawienie go dokładnie raz jest oczywiście optymalne.
* **Nierówne litery**: dowolny superciąg musi zawierać jeden z trzech ostatnich znaków; dlatego ≥ jedno z `DP[i-1][j][k]`, `DP[i][j-1][k]`, `DP[i][j][k-1]` stanowi prefiks takiego superciągu. Dodanie `1` znaku gwarantujegórne ograniczenie, a minimum z tych opcji daje dolne => równość.

Back-tracking tworzy ciąg o długości `D[m][n][p]`, więc optymalny. ∎

---

### 4. Złożoność

* **Czas**: `Θ(m·n·p)` – każdą trójkę indeksów odwiedzamy raz.
* **Pamięć**: `Θ(m·n·p)`; w praktyce da się zwinąć do dwóch warstw `O(n·p)` kosztem trudniejszej rekonstrukcji (przechowywanie znaczników ruchu lub pełna rekonstrukcja w drugim przebiegu).

---

#### Uwaga praktyczna

Dla `m,n,p ≤ 100` algorytm 3D działa natychmiast; przy większych danych warto:

* redukować wymiar (np. **Hirschberg** 2× dzieli-i-zszywaj dla 2D) albo
* heurystycznie łączyć najpierw dwie sekwencje → wynik z trzecią (niegwarantowana optymalność, ale szybciej).

Tak skonstruowany algorytm spełnia wymagania: najkrótszy superciąg dla dwóch, a następnie dla trzech ciągów, z pełnym uzasadnieniem i analizą kosztów.
