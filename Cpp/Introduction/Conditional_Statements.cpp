/* Conditional Statements

Given a positive integer denoting n, do the following:

If 1 <= n <= 9, then print the lowercase English word corresponding to the number (e.g., one for 1, two for 2, etc.).
If n > 9, print Greater than 9.

Input Format
A single integer denoting n.

Constraints
1 <= n <= 10^9

Output Format
If 1 <= n <= 9, then print the lowercase English word corresponding to the number (e.g., one for 1, two for 2, etc.); otherwise, print
Greater than 9 instead. */


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int N;
    cin >> N;
    if (N == 1) {
        cout << "one" << endl;
    } else if (N == 2) {
        cout << "two" << endl;
    } else if (N == 3) {
        cout << "three" << endl;
    } else if (N == 4) {
        cout << "four" << endl;
    } else if (N == 5) {
        cout << "five" << endl;
    } else if (N == 6) {
        cout << "six" << endl;
    } else if (N == 7) {
        cout << "seven" << endl;
    } else if (N == 8) {
        cout << "eight" << endl;
    } else if (N == 9) {
        cout << "nine" << endl;
    } else {
        cout << "Greater than 9" << endl;
    }
 
   return 0;
}
