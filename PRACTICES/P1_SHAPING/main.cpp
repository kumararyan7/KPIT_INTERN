#include"Shape.h"

int  main(){
    Shape circle(ShapeType:: Circle,10,20,30,40,Color::Green,FillPattern::Dotted);
    circle.printAttributes();

    Shape rectangle(ShapeType::Rectangle,50,60,70,80);
    rectangle.printAttributes();

    Shape triangle(ShapeType::Triangle,5,10,15,20 ,Color::Blue,FillPattern::Striped);
    Shape movedTriangle =std:: move(triangle);
    movedTriangle.printAttributes();

    return 0;
}