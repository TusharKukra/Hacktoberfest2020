#include<iostream>
using namespace std;
int main(){
int i=0,j;
int t;
cin>>t;

        int n;
    int arr1[n],arr2[n];
    int num1,num2;
    cin>>num1>>num2;
    while(num1>0)
{
    arr1[i]= num1%2;
    i++;
    num1= num1/2;
}
while(num2>0)
{
    arr2[i]= num2%2;
    i++;
    num2= num2/2;
}

int num3;
num3= num1&num2;

num3= num3>>1;
int num4;
num4= num1 ^ num2;

num4= num3 & num4;
num3= num3^ num4;
cout<<num3;



return 0;
}
