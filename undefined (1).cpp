#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){

int t;
cin>>t;

while(t--){

    int k;
    cin>>k;
    char arr[8][8];
    
    for(int i=0;i<8;i++){
        for(int j=0;j<8;j++){


        arr[i][j]='X';
    }
}
  if(k<=8){
  arr[0][0]='O';
  for(int i=1;i<k;i++){
      for(int j=0;j<8;j++){
          
          arr[i][j]='.';
      }
  }
      
  }  
else if(k>8 &&k <64)


if (k==64){

    for(int i=0;i<8;i++){

        for(int j=0;j<8;j++){
            arr[i][j]='.';
        }
    }
    arr[4][4]='O';
}
else{
     for(int i=1;i<k;i++){

        for(int j=0;j<k;j++){
            arr[i][j]='.';
        }
    }
    
}
    for(int i=0;i<8;i++){

        for(int j=0;j<8;j++){
            cout<<arr[i][j];
        }
        cout<<endl;
}

}
}