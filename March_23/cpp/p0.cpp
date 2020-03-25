#include <iostream>
#include <unordered_map>

using namespace std;

typedef unordered_map<int, int> umap;
typedef vector<int> vi;

int solve(vi& a) {
	int n = a.size();
	umap m;
	for (auto t : a) {
		m[t] += 1;
	}
	int res = 0;
	for (auto t : m) {
		res += (t.second-1)*(t.second);
	}
	return n+res/2;
}
int main() {
	int TC;
	cin>>TC;
	vi output(TC);
	for (int q = 0; q < TC; q++) {
		int n;
		cin >> n;
		vi arr(n);
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		output[q] = solve(arr);
	}
	for (auto t : output) {
		cout << t << endl;
	}
}
