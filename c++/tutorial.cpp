// caleb curry tutorial on yotube

// C++ -> compilation + linking -> executable (or library)

// 2 big things introduced by C++
// OOP
// Generic Programming

// C++ vs C
// C++ came after C (superset of C)
// C++ has more optimization options, used for game engines, softwares, etc
// basically for anything computationally heavy

// now just create a function which works for testing
// the code below will be edited as the tutorial goes on


#include <iostream> // input output stream

// using namespace std; // so you don't have to specify std below

using std::cout; // a declaration, good beacause std only applied to cout
// this will apply to the ENTIRE program
using std::cin;
using std::endl;

// int main() // int specifies return type
// { 
//     int slices;
//     cout << "Sup man, how many slices do you want?: ";
//     cin >> slices; // declaration, then initialization
//     cout << "You have " << slices << " slices of pizza." << std::endl;

// }

// namespace: a grouping of code (prefix to determine specificity of a function)
// also prevents naming conflicts

// object: a tool you use to reach the console
// objects are created from classes (instance?)
// e.g. cout is from ostream

// done with some simple c++ concepts
// 5. Using Directive and Declaration


// 6. Using variables with cout 
// do string concatenation
// output with cout

// 7. User input with cin

// 8. Conventions and Style Guides
// c++ is CASE-SENSITIVE
/* for multiline comment
asd 
asdads
*/ 
// UNDERSCORE STYLE NAMES ARE PREFERRED! 
// there's a style guide by the C++ author on github

// 11. Intro to Creating Custom Functions
// example custom functions

// int multiply(int x, int y)
// {
//     return x + y;
// }


// // 12. Using functions (pow functions)
// #include <cmath>

// double power(double base, int exponent)
// {
//     double result = 1;
//     for(int i = 0; i < exponent; i++)
//     {
//         result = result * base;
//     }
//     return result;
// }                                      

// void print_pow(double base, int exponent)  // void keyword specifies the function does not return a value after its execution
// {
//     double myPower = power(base, exponent); // how to use a return value from the pow function
//     cout << base << " raised to the " << exponent << " power is " << myPower << ".\n" << endl;   //endl here prints an empty line after printing power
// }


// int main()
// {
//     double base;
//     int exponent;
//     cout << "What is the base?: ";
//     cin >> base;
//     cout << "What is the exponent?: ";
//     cin >> exponent;
//     print_pow(base, exponent);
//     print_pow(100, 4);
//     print_pow(4, 2);
// }



// 13. Creating custom functions
// don't use same variable names within the same curly braces

// 14. Creating Void Functions

// 15. Data Types
// every data type must be specified in C++
// C++ is a statically typed programming language, unlike javascript
// e.g. of types: string, integral, char, floating point, bool, arrays, structs, classes
// integral - int
// char - characters
// bool - T/F
// class - a blueprint which describes a structure
// object - an instance of the class

// 16. Integral Data Types and Signed vs Unsigned
// size is not always the same e.g. int x = 5, takes certain amount of memory/space
// size of an int is 32 bits (usually), but guaranteed to be 16 bit
// size of memory can change depending on the system you're on
// 16 bits means...it has 16 ones and zeros
// when you add 1 bit, that's gonna double the total possible values
// point: a 32 bit number has wayyy more combinations than just 2 times that of a 16 bit number
//
// WHAT ABOUT NEGATIVE NUMBERS?
// sign bit, benefit, allows negative numbers but cuts the highest number in half
// the range of values shifts toward the left
// so know if you're working with negative numbers or not (can use unsigned)
// if unsure, just use int

// 17. Integral Data Types, sizeof, climit
//
#include <climits> // helps you figure out the max value that can be stored

// int main()
// {
//     // short <= int <= long <= long long
//     short a;
//     int b; 
//     long c; 
//     long long d; 
//     unsigned short aa;
//     unsigned int bb;
//     unsigned long cc;
//     unsigned long long dd;

//     cout << SHRT_MIN << endl;
// }

// 18. char Data Type
// to store characters OR numbers (THEY ARE RELATED!)
// HINT: ASCII table
// max value is 127, anything bigger, will become negative and start all over from the left
// is use unsigned char, up to 255

// int main()
// {
//     unsigned char x = 129;
//     cout << x;
// }


// 19. Escape Sequences
// special characters that are interpreted, nor printed when in a string
// \v is a vertical tab
// \0: the null terminating character, indicate the end of C style string
// what about if you wanna print backslash? do double backslash :p

// int main()
// {
//     cout << "\"Hello\" there";
// }

// 20. BOOL

// int main()
// {
//     bool found = 1;
//     cout << std::boolalpha << found << endl; // to print out true or false instead of 0/1
// }


// 21. Floating Point Numbers
// 3 types of floating point numbers
// float, double, long double
// floating point numbers are trustworthy until a certain number of digits
// double recommended by default
// if you need to work with moreee decimal places, check out some libraries

#include <float.h> // to see the max number of decimals

// int main()
// {
//     int cents = 100; // can do this when dealing with money to solve accuracy issues
//     float a = 10.0/3;
//     a = a * 10000000000; // least trustworthy, notice that result isn't accurate 
//     double b = a * 10000000000; //7.7E4
//     long double c;

//     cout << std::fixed << a << endl;
//     cout << LDBL_DIG << endl;
// }

// 22. Constant const, macro, enum
// symbolic constants: use "const"

// #define X 10 //another way to define a constant, done in C, valid in C++ too, but
//const is preferred, because it's scoped to a particular block, scoping is generally good

// int main()
// {
//     const int x = 5; // read-only variable
    
//     enum { y = 100 }
// }

// 23. Numeric function
// remainder function similar to modulus operator
// difference, modulus operator always gives us integer!
// remainder function supports float
// check out fmod function too!
// fmax
// fmin
// floor, similarly trunc 
// floor lowers the value to lower integer, trunc literally truncates the decimal
// round(-1.49), .5 or higher, rounding to the next whole number, remember there are many types of rounding
// nearbyint? another tool for rounding
// for more, look up the docs

#include <cmath> // to get sqrt (square root) to work

// int main()
// {
//     cout << trunc(-1.5) << endl;
// }

// 24. String Class and C strings
// easier to deal with C++ strings than those of C


#include <string> // gives access to string class!
 
using std::string; // need this namespace to make string work!

// int main()
// {
//     string greeting = "hello";
//     string complete_greeting = greeting + " there";
//     complete_greeting += "!";
//     cout << complete_greeting << endl; // starts from 0!
//     cout << complete_greeting.length() << endl; // length is a member of the string class! 
//     //method == member function == functions attached to objects
// }

// how to get string from user input?:
// int main()
// {
//     string greeting;
//     cin >> greeting;
//     cout << greeting << endl; // this results in issue if user inputs a string with space! solve it next section
// }

// 25. getline for strings (getting string inputs)

// int main()
// {
//     string greeting;
//     getline(cin, greeting); // for strings
//     cout << greeting << endl;
//    // cin.getline() // to get numbers
// }

// 26. String Modifier Methods
// insert(index, string)
// erase()
// length()
// size()
// pop_back(): to remove last character at the end of string
// replace(first, length from first, "string" )


// int main()
// {
//     string greeting = "Hello!";
//     // greeting += "there"; // another way to do it?
//     greeting.replace(0, 6, "Yeah");
//     cout << greeting << endl;
// } // how to search a string to search a particular word?? next part

// 27. String Operation Methods
// find()
// substr()
// find_first_of()
// compare(): returns 0 if equal, you can also just compare strings with ==

// int main()
// {
//     string greeting = "What is up?";
//     //greeting.replace(greeting.find("hell"), 4, "****"); // this would censor the word "hell"
//     // cout << greeting.find_first_of("aeiou") << endl;
//     if(greeting.compare("What is up?") == 0) cout << "Equals" << endl; // another method to compare strings
// }  // you will see the .compare() in Java.

// 28. Literals 
// 3 types of constants: literal, symbolic, macro
// char32_t (important for developing)
// 5U, the U makes it an unsigned integer
// example auto x = 5U; THIS IS A C++11 extension! x still has a data type

// int main()
// {
//     auto x = 5U; // or 5UL for unsigned long, ULL for unsigned long long, F for float, nothing for double, L for long double
//     // x = "this is a string"; // this wouldn't work
// }


// 29. Hex and Octal
// hex: 0 - 15, and then a new position, and so on
// octal: 0 - 7, and then a new position, and so on 
// 

int main()
{
    int number = 030; // will get 24
    cout << number << endl;
}   // make sure you understand hex and octal (memory addresses and so on)


// 30. Operator Precedence and Associativity

