#include<bits/stdc++.h>
using namespace std;

typedef long long i64;
constexpr i64 mod = 1e9 + 7;
constexpr i64 q = 127; // dzięki temu nie trzeba robić (string[i] - 'a') (bo jest to liczba pierwsza > ord('z'))

i64 bin_pow(i64 a, i64 pow) { // normalnie to się tablicuje a nie oblicza; (w sumie to ogarnołem teraz że wystarczy nam tylko pamiętać q**(m - 1))
    i64 ans = 1;
    while(pow) {
        if(pow % 2) ans *= a, ans %= mod;
        a *= a;
        pow /= 2;
    }

    return ans;
}

class Karp_rabin {
private:
    const string &text, &pattern;
    int n, m;
    i64 hsh_text = 0, hsh_pattern = 0;

    void initialize_hsh() {
        for(int i = 0; i < m; i++) {
            hsh_text = (hsh_text * q + text[i]) % mod;
            hsh_pattern = (hsh_pattern * q + pattern[i]) % mod;
        } 
    }

    void hsh_roll(int idx) { // dodaje następny charakter i usówa frontowy charakter
        hsh_text -= (text[idx - m]) * bin_pow(q, m - 1);
        hsh_text = (hsh_text + mod) % mod;
        hsh_text = (hsh_text * q + text[idx]) % mod;
    }

public:
    Karp_rabin(const string &text, const string &pattern)
        : text(text), pattern(pattern) {
        n = text.size();
        m = pattern.size();

        initialize_hsh();
    }

    i64 count_occurences() { 
        i64 ans = hsh_pattern == hsh_text;
        for(int i = m; i <= n; i++) {
            hsh_roll(i);
            ans += hsh_pattern == hsh_text; // tutaj zazwyczaj jeszcze sprawdzmy czy text[] == pattern[] liniowo jeśli hsh sie zgadzają 
        }

        return ans;
    }
};

int main() {
    string text, pattern; cin >> text >> pattern;
    Karp_rabin karp_rabin(text, pattern);
    cout << karp_rabin.count_occurences() << endl;
}

