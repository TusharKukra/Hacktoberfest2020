#include<bits/stdc++.h>
using namespace std;
int main(){
	int a, nums, y,i,x;
	set<int>s;
	cout<<"Enter the no of queries: "<<endl;
	cin>>a;
	for(i=0; i<=a-1; i++){
		cout<<"Enter the type of query: "<<endl;
		cin>>y>>x;
		if(y==1){
			s.insert(x);
		}
		else if(y==2){
			s.erase(x);
		}
		else{
			cout << (s.find(x) == s.end() ? "No" : "Yes") << endl;
			}
		}
	return 0;
}
