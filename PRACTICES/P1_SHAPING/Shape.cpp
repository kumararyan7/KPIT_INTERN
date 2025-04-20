#include "Shape.h"



Shape::Shape(ShapeType t, int x, int y, int w, int h, Color c, FillPattern f)
:type(t),x(x),y(y),width(w),height(h),color(c),fillPattern(f){}

Shape::Shape(ShapeType t, int x, int y, int w, int h, Color c):
Shape(t,x,y,w,h,c,FillPattern::Solid){}

Shape::Shape(ShapeType t, int x, int y, int w, int h):
Shape(t,x,y,w,h,Color::Red,FillPattern::Solid){}

Shape::Shape(ShapeType t, int x):
Shape(t,x,0,0,0,Color::Red,FillPattern::Solid){}

Shape::Shape(ShapeType t, int x, int y)
:Shape(t,x,y,0,0,Color::Red,FillPattern::Solid){}

Shape::Shape(Shape &&other) noexcept:
type(other.type),x(other.x),y(other.y),width(other.width),height(other.height),color(other.color),fillPattern(other.fillPattern){}

Shape &Shape::operator=(Shape &&other) noexcept
{
    if (this != &other){
        type = other.type;
        x = other.x;
        y=other.y;
        width= other.width;
        height = other.height;
        color= other.color;
        fillPattern = other.fillPattern;
    } 
    // TODO: insert return statement here
    return *this;
}

ShapeType Shape::getType() const { return type; }
int Shape::getX() const { return x; }
int Shape::getY() const { return y; }
int Shape::getWidth() const { return width; }
int Shape::getHeight() const { return height; }
Color Shape::getColor() const { return color; }
FillPattern Shape::getFillPattern() const { return fillPattern; }

void Shape::printAttributes() const {
    std::cout << "ShapeType: " << static_cast<int>(type)
              << ", x: " << x << ", y: " << y
              << ", width: " << width << ", height: " << height
              << ", color: " << static_cast<int>(color)
              << ", fillPattern: " << static_cast<int>(fillPattern) << "\n";
}

