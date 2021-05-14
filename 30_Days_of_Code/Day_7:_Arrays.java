import java.io.*;
import java.util.Scanner;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
     
        Scanner input = new Scanner(System.in);
         int n = input.nextInt();
         int[] arr = new int[n];
         for(int i=0; i<n; i++){
             arr[i]=input.nextInt();
         }        
         for(int i=(arr.length-1); i>=0; --i){
 
             System.out.print(arr[i]+ " ");
         }

        bufferedReader.close();
    }
}
