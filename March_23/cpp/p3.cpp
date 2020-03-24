#include <iostream>
#include <string>
#include <unordered_map>


using namespace std;
typedef long long ll;

ll solve(string& s) {
	int base = 0;
	unordered_map<char, int> hm;
	int val = 0;
	for (auto t : s) {
		if (hm.find(t) == hm.end()) {
			hm.insert({t,val++});
			base++;
		}
	}
	hm[s[0]] = 1;
	for (auto t : s) {
		if (t != s[0]) {
			hm[t] = 0;
			break;
		}
	}
	
	ll res = 0;
	ll nbase = 1;
	for (int i = s.size() - 1; i >= 0;--i) {
		res += nbase * hm[s[i]];
		nbase *= base;
	}
	
	return res;
}
int main() {
	int TC;
	cin >> TC;
	vector<int> output(TC);
	for (int q = 0; q < TC; ++q) {
		string s;
		cin >> s;
		output[q] = solve(s);
	}
	for (auto t : output) {
		cout << t << endl;
	}
	
}