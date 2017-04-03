/* Inheritance Introduction

One of the important topics of Object Oriented Programming is Inheritance. Inheritance allows us to define a class in terms of another
class, which allows us in the reusability of the code. Check out the code below:

class Triangle{
    public:
        void triangle(){
            cout<<"I am a triangle\n";
        }
};

The class Triangle has a function called triangle(). Now we create a class derived from the base class Triangle called Isosceles.

class Isosceles : public Triangle{
    public:
        void isosceles(){
            cout<<"I am an isosceles triangle\n";
        }
};

Now we can create a derived class object and use it to access the functions of the base class.

int main(){
    Isosceles isc;
    isc.isosceles();
    isc.triangle();
    return 0;
}

This code will print:

I am an isosceles triangle
I am a triangle
Now write a function in Isosceles class such that the output is as given below.

Sample Output

I am an isosceles triangle
In an isosceles triangle two sides are equal
I am a triangle */


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


class Triangle{
    public:
       void triangle(){
           cout<<"I am a triangle\n";
       }
};
class Isosceles : public Triangle{
    public:
       void isosceles(){
          cout<<"I am an isosceles triangle\n";
       }
        //Write your code here.
        void description(){
            cout<<"In an isosceles triangle two sides are equal\n";
        }
};
int main(){
    Isosceles isc;
    isc.isosceles();
     isc.description();
    isc.triangle();
    return 0;
}
