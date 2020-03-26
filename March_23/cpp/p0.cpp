// PROBLEM - FINDING PAIRS
// O(N) SOLUTION

#include <iostream>
#include <unordered_map>

using namespace std;

typedef unordered_map<int, int> umap;				
typedef vector<int> vi;
typedef long long ll;

ll solve(vi& a) {
	int n = a.size();					// store all the elements in a hashmap as (element,frequency) pairs
	umap m;							// if an element appears 't' times then pairs would be t*(t-1)/2
	for (auto t : a) {					// also we need to add every element itself so n + sigma(t*(t-1)/2)
		m[t] += 1;					
	}							
	ll res = 0;
	for (auto t : m) {
		res += (ll)(t.second-1)*(t.second);		// if t = 10^6 then t*(t-1) exceeds 10^12 so make sure to use 64-bit int
	}
	return n+res/2;
}
int main() {
	int TC;										
	cin>>TC;						// reading no of test cases.
	vi output(TC);						// variable to store outputs. 
	for (int q = 0; q < TC; q++) {
		int n;
		cin >> n;
		vi arr(n);
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		output[q] = solve(arr);				// make sure to pass reference instead of a new copy for
								// better performance.
	}
	for (auto t : output) {
		cout << t << endl;				// printing output.
	}
}
