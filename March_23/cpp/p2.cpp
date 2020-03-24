#include <iostream>
#include <vector>


using namespace std;
typedef vector<vector<int>> vec2d;


int solve(vec2d& grid, vec2d visited,int n,int x = 0,int y = 0) {
	if (x > n - 1 || y > n - 1) { return 0; }
	if (x == n - 1 && y == n - 1) {	return 1;}
	if (grid[x][y] == 1) { return 0; }
	visited[x][y] = 1;
	vec2d tmp = visited;
	int cres = 0;
	if (x != n - 1 && !visited[x + 1][y])
		cres += solve(grid, tmp, n, x + 1, y);
	if(x != 0 && !visited[x-1][y])
		cres += solve(grid,tmp,n, x - 1, y);
	if(y != n-1 && !visited[x][y+1])
		cres += solve(grid,tmp,n, x, y+1);
	if(y != 0 && !visited[x][y-1])
		cres += solve(grid,tmp,n, x, y-1);
	return cres;
}
int main() {
	int TC;
	cin >> TC;
	vector<int> output(TC);
	for (int q = 0; q < TC; ++q) {
		int n;
		cin >> n;
		vector<vector<int>> grid(n, vector<int>(n, 0));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> grid[i][j];
			}
		}
		vec2d zeroes(n, vector<int>(n, 0));
		output[q] = solve(grid,zeroes,n);
	}
	for (auto t : output) {
		cout << t << endl;
	}
}