#include <iostream>
using namespace std;
#include <vector>
#include <string>

bool scheck(char* s, int start, int end){
    assert(start >=0 );
    for(int i=start; i<end; i++){
        if(s[i] != s[end - i + start]){
            return false;
        }
    }
    return true;
}

int main(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    int arr[n+1];
    arr[0] = 0;
    arr[1] = 1;
    for(int i = 2; i <= n; i++){
        for(int j = 0; j < i-1; j++){
            if( scheck(s, j, i-1) ){
                if(arr[] < arr[i-1])
            }
        }
    }

}


