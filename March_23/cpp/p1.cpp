#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool char_in(string& s, char c) {
	for (auto t : s) {
		if (t == c) {
			return true;
		}
	}
	return false;
}
bool solve(string& word, string& p) {
	int n = word.size();
	vector<string> pp;
	for (int i = 0; i < p.size(); i++) {
		if (p[i] == '(') {
			i++;
			string tmp = "";
			while (p[i] != ')' && i < p.size()) {
				tmp += p[i];
				i++;
			}
			pp.push_back(tmp);
			continue;
		}
		string tmp = "";
		tmp += p[i];
		pp.push_back(tmp);
	}
	
	for (int i = 0; i < n; i++) {
			if(!char_in(pp[i],word[i])){
				return false;
			}
			
	}
	return true;
}
int main() {
	int N,D,TC;
	cin >> N;
	cin >> D;
	cin >> TC;
	vector<int> output(TC);
	vector<string> words(D);
	for (int i = 0; i < D; i++) {
		cin >> words[i];
	}
	for (int q = 0; q < TC; q++) {
		string pat;
		cin >> pat;
		int res = 0;
		for(auto t : words){
			res += solve(t, pat);
		}
		output[q] = res;
	}
	
	for (auto t : output) {
		cout << t << endl;
	}
}
