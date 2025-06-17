class UnionFind:
    """DSU z union-by-size i kompresją ścieżek."""
    def __init__(self, n: int):
        """
        Tworzy n rozłącznych jednoelementowych zbiorów.

        Args:
            n (int): liczba elementów (oznaczamy je 0..n-1)
        """
        self.parent = list(range(n))   # rodzic lub korzeń
        self.size   = [1] * n          # rozmiar drzewa dla korzeni

    def find(self, x: int) -> int:
        """
        Zwraca reprezentanta (korzeń) zbioru zawierającego x,
        stosując kompresję ścieżek.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        """
        Łączy zbiory zawierające elementy a i b.

        Returns:
            bool: True jeśli zbiory były rozłączne i zostały połączone,
                  False jeśli już były w tym samym zbiorze.
        """
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # już w tym samym zbiorze

        # union by size – mniejszy podwieszamy pod większy
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra  # zamiana tak, by ra był większy

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def connected(self, a: int, b: int) -> bool:
        """Sprawdza czy a i b leżą w tym samym zbiorze."""
        return self.find(a) == self.find(b)

    def set_size(self, x: int) -> int:
        """Zwraca rozmiar zbioru, w którym jest element x."""
        return self.size[self.find(x)]
