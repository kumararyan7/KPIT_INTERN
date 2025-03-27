//Write a C++ program to declare and initialize an array of integers.

#include<iostream>

// int main(){
//     int arr[5]= {1,2,3,4,5};
//     for(int i =0;i<5;i++){
//      std:: cout<< arr[i]<< std ::endl;
//     }
//     return 0;

// }
using namespace std;
int main(){
    int numbers[5];
    
    cout << "Enter 5 numbers: ";
    for (int i = 0; i < 5; i++) {
        cin >> numbers[i];
    }
    
    cout << "You entered: ";
    for (int i = 0; i < 5; i++) {
        cout << numbers[i] << " ";
    }
    
    return 0;
}
