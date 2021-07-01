/* Java If-Else

In this challenge, we test your knowledge of using if-else conditional statements to automate decision-making processes.

Task 
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format
A single line containing a positive integer, n.

Constraints
1 <= n <= 100

Output Format
Print Weird if the number is weird; otherwise, print Not Weird. */


import java.io.*;
    import java.util.*;
    import java.text.*;
    import java.math.*;
    import java.util.regex.*;

    public class Solution {

        public static void main(String[] args) {

            Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        if(n % 2 == 1 || (n >= 6 && n <=20)) {
            System.out.println("Weird");
        }
        else {
          System.out.println("Not Weird");
        }
            
        }
    }
