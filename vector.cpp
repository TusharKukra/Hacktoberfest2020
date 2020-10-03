#include<bits/stdc++.h>
#include<iostream>
using namespace std;

bool c(int x,int y){
    return x>y;
}
void vectordemo(){
    // c++ stl


    // coding is fun

    vector<int>A={1,2,3,4,23,45,232,123};
    // access the element 

    cout<<A[2]<<endl;


    sort(A.begin(),A.end()); //nlogn 

// binary search

bool present = binary_search(A.begin(),A.end(),3);

present= binary_search(A.begin(),A.end(),6);

vector<int> a;
a.push_back(100);
a.push_back(100);
a.push_back(100);
a.push_back(100);
a.push_back(100);
a.push_back(100);
a.push_back(123);
a.push_back(1767);
a.push_back(543);



auto it= lower_bound(a.begin(),a.end(),100);
vector<int>:: iterator it1= upper_bound(a.begin(),a.end(),100);

  cout<<*it<<" "<< *it1<<endl;
cout<<it1-it<<endl;
// Vector sorted in decreasing order
sort(a.begin(),a.end(),c);
vector<int>:: iterator it2;

for(it2= a.begin();it2!=a.end();it2++ ){
    cout<<*it2<<endl;
}

cout<<"Increasing order sort"<<endl;
sort(a.begin(),a.end());
for(int x: a ){
    cout<<x<<endl;
}    
}

void setdemo(){


    // in set there is no need of sorting the array its already sorted no 
    // matter in what order you have insert the elements complx logn i love you set form now
    set<int>s;
    s.insert(19);
    s.insert(27);
    s.insert(12);
    s.insert(15);
    s.insert(14);
    s.insert(17);
    s.insert(18);
    s.insert(11);
    s.insert(193);
    s.insert(-1);
    for(int x: s){
        cout<<x<<endl;
    }

    auto it= s.find(-1);
    if(it== s.end()){
        cout<<"Not present\n";
    }
    else{
        cout<<"present\n";
        cout<<*it<<endl;
    }

    auto it2= s.upper_bound(-1);
    auto it3= s.upper_bound(11);
    cout<<*it2<<" " <<*it3<<endl;


    auto it4= s.upper_bound(14);
    if(it4== s.end()){
        cout<<"not present\n";
    }
    else{
        cout<<"present\n";
        s.erase(it4);
    }
// for erasing an element from the set we can use the below method
    s.erase(27);
    for(int a: s){
        cout<<a<<endl;
    }
}

void map_demo(){
    map<int ,int>mp;

    mp[1]=100;
    mp[2]=2893;
      mp[3]=2293;
        mp[4]=93;
        map<char, int> cnt;
        string x= "Hunny sunaria";

        for(char c:x){
            cnt[c]++;
        }

        cout<<cnt['a']<<" "<<cnt['s']<<endl;
cnt.erase('s');
   
}

// void powerofstl(){
//     // add[2,3];
//     // add[10,20];
//     // add[23,56];

//     set<pair<int, int>> s;
//     s.insert({2,3});
//     s.insert({10,20});
//     s.insert({23,56}); 

//     vector<int> :: iterator it;
//    for(int x : s){
//        cout<<x
//    }
// }

int main(){
    map_demo();
    return 0;
}