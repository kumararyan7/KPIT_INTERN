// Develop a C++ program to input and display the values of different data types.

#include<iostream>

int main (){

    int n;
    double f;
    bool isTrue;
    char letter;
    std::string Name;

    std:: cout<< "Enter the integer:"<<std:: endl;
    std::cin>> n;
    std:: cout<< "Enter the decimal:"<<std:: endl;
    std::cin>> f;
    std:: cout<< "Enter the Bool:"<<std:: endl;
    std::cin>> isTrue;
    std:: cout<< "Enter the character:"<<std:: endl;
    std::cin>> letter;
    std:: cout<<"Enter the Name:"<<std::endl;
    std:: cin>>Name;
// Declaring outputs

std:: cout<< "Thr integer is :"<<n<< std:: endl;
std:: cout<< "Thr decimal is :"<<f<< std:: endl;
std:: cout<< "Thr bool is :"<<isTrue<< std:: endl;
std:: cout<< "Thr char is :"<<letter<< std:: endl;
std:: cout <<"The name is :"<< Name<<std:: endl;
}