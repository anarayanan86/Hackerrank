/* Input and Output

Objective 
In this challenge, we're practicing reading input from stdin and printing output to stdout.
In C++, you can read a single whitespace-separated token of input using cin, and print output to stdout using cout. For example, let's
say we declare the following variables:
string s;
int n;
and we want to use cin to read the input "High 5" from stdin. We can do this with the following code:
cin >> s >> n;
The above code reads the first word ("High") from stdin and saves it as string s, then reads the second word ("5") from stdin and saves
it as integer n. If we want to print these values to stdout, we write the following code:
cout << s << " " << n << endl;
The above code prints the contents of string s, which is the word "High". Then it prints a single space (), followed by the contents of
integer n. Because we also want to ensure that nothing else is printed on this line, we end our line of output with a newline via endl.
This results in the following output:
High 5

Task 
Read 3 numbers from stdin and print their sum to stdout.
Note: If you plan on completing this challenge in C instead of C++, you'll need to use format specifiers with printf and scanf.

Input Format
A single line containing 3 space-separated integers: a, b, and c.

Constraints
1 <= a, b, c <= 1000

Output Format
Print the sum of the three numbers on a single line. */


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int a;
    int b;
    int c;
    cin >> a >> b >> c;
    cout << a + b + c << endl;
    return 0;
}
