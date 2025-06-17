#include<bits/stdc++.h>
using namespace std;

typedef long long i64;

class Knuth_morris_patt {
private:
    const string &text, &pattern;
    int n, m;
    vector<int> lps; // inna nazwa to $\pi$

    void precompute_lps() {
        lps.resize(m);
        for(int i = 1; i < m; i++) {
            int j = lps[i - 1];
            while(j and pattern[i] != pattern[j])
                j = lps[j - 1];

            if(pattern[i] == pattern[j]) 
                j++;
            
            lps[i] = j;
        }
    }

public:
    Knuth_morris_patt(const string& text, const string& pattern)
        : text(text), pattern(pattern) {
        n = text.size();
        m = pattern.size();

        precompute_lps();
    }

    i64 count_occurences() {
        i64 ans = 0;
        int j = 0;

        for(int i = 0; i < n; i++) {
            while(j and text[i] != pattern[j])
                j = lps[j - 1];

            if(text[i] == pattern[j])
                j++;
            
            if(j == m) {
                ans++;
                j = lps[j - 1];
            }
        }

        return ans;
    }
};

int main() {
    string text, pattern; cin >> text >> pattern;
    Knuth_morris_patt kmp(text, pattern);
    cout << kmp.count_occurences() << endl;
}
