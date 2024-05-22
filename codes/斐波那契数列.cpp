#include <bits/stdc++.h>

using namespace std;
int fib[25];
int main() {
	fib[1]=fib[2]=1;
	for(int i=3;i<=19;i++)
		fib[i]=fib[i-1]+fib[i-2];
	cout <<fib[19];
	return 0;
}
