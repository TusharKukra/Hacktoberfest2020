#include<bits/stdc++.h>
using namespace std;
 
int main(){
     long long int i,n,a,b;
     cin>>n>>a>>b;
     b%=n;
     if(b==0)
     {
          cout<<a;
     }
     else if(b>0)
     {
          a+=b;
          if(a>n)
          {
               a-=n;
          }
          cout<<a;
     }
     else
     {
          i=-b;
          if(i>=a)
          {
 
               i-=a  ;             a=n-i;
          }
          else
          {
               a-=i;
          }
          cout<<a;
     }
     return 0;
}
