#include<iostream>
#include<stdio.h>
#include<math.h>

using namespace std;
#define N 30

int main()
{
	int n=61;
	double sq=sqrt(n);
	int a[N];
	double x[N];
	
	a[0]=int(sq);
	x[0]=sq-a[0];
	cout<<a[0]<<" ";
	for(int i=1;i<N;i++)
	{
		a[i]=int(1.0/x[i-1]);
		x[i]=1.0/x[i-1]-a[i];
		cout<<a[i]<<" ";
	}
	return 0;
}
