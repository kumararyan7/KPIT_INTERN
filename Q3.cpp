//Write a C++ program to demonstrate the use of const keyword with variables.
#include<iostream>

   const  double PI = 3.14;


    int main(){
        const int Maxspeed = 120;
        const float Gravity = 9.81f;
        const char Initial = 'A';


        std :: cout<< "Global constant PI :"<< PI<< std:: endl;
        std :: cout<< "Maxspeed :"<< Maxspeed<< std:: endl;
        std :: cout<< "Gravity :"<< Gravity<< std:: endl;
        std :: cout<< "Initial :"<< Initial<< std:: endl;
        

return 0;

}
