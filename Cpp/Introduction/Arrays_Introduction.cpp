/* Arrays Introduction

An array is a series of elements of the same type placed in contiguous memory locations that can be individually referenced by adding an
index to a unique identifier.

Declaration:

int arr[10]; //Declares an array named arr of size 10, i.e; you can store 10 integers.
Accessing elements of an array:

Indexing in arrays starts from 0.So the first element is stored at arr[0],the second element at arr[1]...arr[9]
You'll be given an array of N integers and you have to print the integers in the reverse order.

Input Format
The first line of the input contains N, where N is the number of integers. The next line contains N integers separated by a space.

Constraints
1 <= N <= 1000
1 <= Ai <= 10000, where Ai is the ith integer in the array.

Output Format
Print the N integers of the array in the reverse order in a single line separated by a space. */


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
    int arr[N];
    for (int i = 0; i < N; i++) {
        cin >> arr[i];        
    }
    for (int j = N - 1; j >= 0; j--) {
        cout << arr[j] << " ";
    }
    return 0;
}
