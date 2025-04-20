#ifndef UNIVERSITYSTUDENT_H
#define UNIVERSITYSTUDENT_H

#include<string>

class UniversityStudent{
    private:
    std:: string name;
    int age;
    double gpa;
    std:: string major;
    std:: string email;
    std:: string phone;
    std:: string address;

public:
 UniversityStudent();

 UniversityStudent(const std:: string& name, int age);
 UniversityStudent(const std:: string& name, int age , double gpa , const std:: string& major ,
                    const std:: string& email, const std:: string& phone , const std:: string & address;)
}


#endif // UNIVERSITYSTUDENT_H
