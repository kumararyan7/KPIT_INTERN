#ifndef SHAPE_H
#define SHAPE_H

#include"ShapeEnums.h"
#include<iostream>

class Shape{
    private:
    ShapeType type;
    int x,y;
    int width,height ;
    Color color;
    FillPattern fillPattern;

    public:
    //Primary const
    Shape(ShapeType  t , int x, int y  , int w, int h , Color c , FillPattern f);
    // Const with default
    Shape(ShapeType t,int x, int y , int w ,int h ,Color c);
    // Const with default color
    Shape(ShapeType t , int x, int y ,int w,int h );
    // Const with default width, height
    Shape(ShapeType t , int x);
    // 
    Shape(ShapeType t , int x, int y);
    // Deleted copy constructir and assignment
    Shape(const Shape& )= delete;
    Shape& operator = (const Shape&) = delete;

    //Move constructor
    Shape (Shape&& other ) noexcept;

    //move assignmnet operator
    Shape& operator = (Shape&& other )noexcept;

    //Getters
    ShapeType getType() const;
    int getX() const;
    int getY() const;
    int getWidth() const;
    int getHeight() const;
    Color getColor() const;
    FillPattern getFillPattern() const;

    // Utility func
    void printAttributes() const;
};


#endif // SHAPE_H

