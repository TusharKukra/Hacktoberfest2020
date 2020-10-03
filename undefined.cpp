#include <iostream>
#include<bits/stdc++.h>
using namespace std;
// string cnt(vector<int> &nums){
//     vector<int>v;
//     for(int i=0;i<nums.size();i++){
//     v[nums[i]-1]++;
//     }



// for(int i=0;i<v.size();i++)
//     if(v.find(v[i]!= v.end())){
        
//         return "NO";
//     }
    
//     return "YES";
    
// }





int main() {
	// your code goes here
	
	
long long	int t;
	cin>>t;
	
	while(t-->0){
	    
	    
	    
	    long long int n;
	    cin>>n;
	    
	    vector<int> ar(n);
	    
	    for(int i=0;i<n;i++){
	        
	        cin>>ar[i];
	    }
	
unordered_map<int, int>mp;
	
	for(int x:ar){
	    
	    mp[x]++;
	}
	
	for(auto it= mp.begin();it!=mp.end();++it)


if(mp.find(it->second)!=mp.end())
{

cout<<"NO";

break;
}
else{
cout<<"YES";
break;
}

cout<<"\n";
	    
	}   
	    
	

}
