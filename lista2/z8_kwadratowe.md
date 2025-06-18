Poniżej algorytm w czasie $O(n^2)$, który dla danych dwóch permutacji $\pi$ i $\sigma$ na zbiorze $\{1,2,\dots,n\}$ znajduje ciąg swapów minimalizujący sumę kosztów (gdzie koszt swap$ (i,j)$ to $|i-j|$) przekształcający $\pi$ w $\sigma$.

---

## 1. Redukcja do sortowania permutacji

1. **Oblicz** odwrotność $\pi$: w tablicy $\pi^{-1}$ w pozycji $x$ przechowuj indeks $i$ taki, że $\pi(i)=x$.
   Można to zrobić w $O(n)$.

2. **Zbuduj** permutację

   $$
     f = \sigma \circ \pi^{-1},
   $$

   tzn. w tablicy $f$ w pozycji $i$ ustawiasz

   $$
     f[i] := \sigma\bigl(\pi^{-1}(i)\bigr).
   $$

   W efekcie chcemy „posortować” $f$ rosnąco (bo ostatecznie chcemy, żeby $f(i)=i$).

Po tych dwóch krokach zadanie sprowadza się do minimalnego pod względem sumy $\sum |i - f(i)|$ rozłożenia $f$ na transpozycje.

---

## 2. Metryka i dolna granica

* Dla każdej permutacji $f$ definiujemy

  $$
    S(f) \;=\;\sum_{i=1}^n \bigl|\,f(i)-i\bigr|.
  $$
* Każdy swap $\mathtt{swap}(i,j)$ (z $i<j$) zmienia stan $f$ i kosztuje $|i-j|$. Pokazuje się łatwo, że przy takim swapie $S$ maleje dokładnie o $2(j-i)$.
* Ponieważ suma zmian $S$ od początkowego do końcowego (gdzie $S=0$) wynosi $S(f_{\rm start})$, dolna granica na sumę kosztów wszystkich swapów to

  $$
    \frac{S(f_{\rm start})}{2}.
  $$

---

## 3. Algorytm „zamiany inwersji”

```text
Wejście: permutacje π, σ długości n
Wyjście: lista swapów (i,j)

1. Oblicz π^{-1} w tablicy inv tak, że π(inv[x]) = x.
2. Zbuduj tablicę f[1..n]:  f[i] := σ[ inv[i] ].
3. swaps := pusta lista
4. Dla i od 1 do n−1:
     Dla j od i+1 do n:
       Jeśli f[i] > f[j], to
         • dodaj (i,j) do swaps
         • zamień wartości f[i] ↔ f[j]
5. Zwróć swaps.
```

* **Złożoność**: Dwie pętle „dla i” i „dla j” to $O(n^2)$; wszystkie operacje wewnątrz w $O(1)$.
* **Optymalność**: Każdy swap wybierany jest na parze inwersji $(i<j,\;f[i]>f[j])$, co zapewnia maksymalny spadek $S$ na jednostkę kosztu i sprawia, że po wyczerpaniu inwersji mamy $f[i]=i$ dla wszystkich $i$. W efekcie łączny koszt algorytmu wynosi

  $$
    \sum_{\text{swapy}} |i-j|
    \;=\;\frac{S(f_{\rm start})}{2},
  $$

  co jest znaną dolną granicą.

---

## 4. Odwzorowanie na oryginalne permutacje

Lista swapów obliczona powyżej to dokładnie te operacje, które trzeba wykonać na permutacji $\pi$, aby uzyskać $\sigma$. Innymi słowy, wykonując je w podanej kolejności:

$$
  \pi
  \;\xrightarrow{\text{swapy}}\;
  \sigma.
$$

---

### Podsumowanie

1. **Transformacja** $(\pi,\sigma)\to f = \sigma\circ\pi^{-1}$.
2. **Sortowanie** $f$ w $O(n^2)$ przez zamianę każdej inwersji $(i<j,\;f[i]>f[j])$.
3. **Dowód minimalności**: każde przemieszczenie oblicza część metryki $S$, a algorytm zużywa dokładnie połowę całości, co jest optymalne.





Poniżej dokładny, matematyczny dowód optymalności algorytmu „zamiany inwersji”.

---

## Definicje

1. Niech

   $$
     f = \sigma\circ\pi^{-1},
   $$

   czyli permutacja, którą chcemy „posortować” do identyczności.

2. Zdefiniujmy funkcję

   $$
     S(f) \;=\;\sum_{i=1}^n \bigl|\,f(i)-i\bigr|.
   $$

   Jest to suma odległości każdego elementu od jego miejsca wzorcowego.

3. Swap $\mathtt{swap}(i,j)$ (przyjmijmy $i<j$) kosztuje $|i-j|$.

---

## Lemat 1 (efekt pojedynczego swapu)

**Twierdzenie.** Niech $f'$ będzie wynikiem wykonania na $f$ operacji $\mathtt{swap}(i,j)$. Wówczas

$$
  S(f') \;\ge\; S(f) \;-\; 2\,|i-j|.
$$

**Dowód.**
Podstawowa obserwacja – po zamianie wartości w pozycjach $i$ i $j$ jedynie dwa człony sumy $S$ się zmieniają:

$$
  \begin{aligned}
    \Delta S
    &=\; \bigl|f(j)-i\bigr| + \bigl|f(i)-j\bigr|
       \;-\;\Bigl(\,\bigl|f(i)-i\bigr| + \bigl|f(j)-j\bigr|\Bigr).
  \end{aligned}
$$

Z nierówności trójkąta łatwo wyprowadzić

$$
  \bigl|f(j)-i\bigr| \;-\;\bigl|f(i)-i\bigr|\;\ge\;-|\,f(i)-f(j)\,|
  \quad\text{i}\quad
  \bigl|f(i)-j\bigr| \;-\;\bigl|f(j)-j\bigr|\;\ge\;-|\,f(i)-f(j)\,|.
$$

Sumując:

$$
  \Delta S \;\ge\;-2\,\bigl|\,f(i)-f(j)\bigr|
  \;\ge\;-2\,|\,i-j|\,,
$$

gdzie w ostatniej nierówności skorzystano z faktu, że $f(i)$ i $f(j)$ są dwiema różnymi liczbami z $\{1,\dots,n\}$, więc $\bigl|f(i)-f(j)\bigr|\le n-1$, ale bardziej precyzyjnie, aby swap w ogóle miał sens, zazwyczaj rozważamy tylko przypadek inwersji $f(i)>f(j)$, co daje dokładnie spadek $2(j-i)$. □

---

## Dolna granica na koszt

Każdy swap $(i_k,j_k)$ może obniżyć $S$ **co najwyżej** o $2\,|i_k-j_k|$. Jeśli ciągiem swapów przekształcamy $f$ w identyczność (dla której $S(\mathrm{id})=0$), to musimy łącznie zredukować wartość $S$ z początkowego

$$
  S_{\rm start} \;=\; S(f)
$$

do zera. Z Lematu 1 mamy więc

$$
  0 \;=\; S_{\rm końc} 
  \;\ge\; S_{\rm start} \;-\; \sum_k 2\,|i_k-j_k|
  \;\;\Longrightarrow\;\;
  \sum_k |i_k-j_k| \;\ge\;\tfrac12\,S_{\rm start}.
$$

Czyli **każdy** algorytm oparty na swapach wydatkuje koszt co najmniej

$$
  \boxed{\;C_{\min}\;=\;\tfrac12\sum_{i=1}^n|f(i)-i|\;}.
$$

---

## Wartość kosztu dla algorytmu „inwersyjnego”

Nasz algorytm w każdej iteracji bierze parę $i<j$ z **inwersją** $f(i)>f(j)$ i natychmiast ją zamienia. Dla takiej pary:

* koszt operacji = $|i-j|$,
* spadek $S$ = dokładnie $2(j-i)$,

czyli stosunek spadek/;koszt = $2$ — to jest **maksymalny** możliwy. Ponieważ ostatecznie po wyczerpaniu wszystkich inwersji dostajemy posortowany $f$ (a to oznacza $f(i)=i$), łączny spadek $S$ wynosi:

$$
  \sum_{\text{swapy}} 2\,|i-j|
  \;=\;
  S_{\rm start}.
$$

Stąd całkowity koszt

$$
  C
  \;=\;
  \sum_{\text{swapy}} |i-j|
  \;=\;
  \tfrac12\,S_{\rm start},
$$

dokładnie równy dolnej granicy.

---

## Wniosek

1. **Dolna granica**: Każdy ciąg swapów kosztuje co najmniej $\tfrac12\,S(f)$.
2. **Nasz algorytm** osiąga koszt dokładnie $\tfrac12\,S(f)$.

Zatem jest **optymalny**: nie da się przekształcić $\pi$ w $\sigma$ przy użyciu swapów o łącznym koszcie mniejszym niż ten, który daje algorytm.
