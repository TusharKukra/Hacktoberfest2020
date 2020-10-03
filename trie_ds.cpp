
#include <iostream>
#include<bits/stdc++.h>
using namespace std;


// structure of trie node
struct trie{
    struct trie *child[26];
    bool isend;

    trie(){
        memset(child,0,sizeof(child));
        isend= false;
    }
};




struct trie *root;

void inserta(string word){ // inserting new charac into the trie node
    trie *current = root;
    for(char ch: word){

        int indx= ch-'a';
        if(current->child[indx]== NULL){
            current->child[indx]= new trie;
        }
        current= current->child[indx];
    }
    current ->isend= true;


}

bool searcha(string word){   //search for string present in the trie
// if i search for abcd then it return value on the basis of isend or presence of value
    trie *cur= root;
    for(char ch: word){

        int indx= ch-'a';
        if(cur->child[indx]== NULL){
            return false;
            cur= cur->child[indx];
        }
    }
    return cur->isend;
}

int main() {
	// your code goes here

	root= new trie;
	long long int n;

	cin>>n;
	while(n--){

	    string str;
	    cin>>str;
	    inserta(str);
	}
	cin>>n;
	while(n--){
        string str;
        cin>>str;
        if(searcha(str))

            cout<<" Present ";

        else
            cout<<" Not present";

	}
}
