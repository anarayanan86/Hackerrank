import java.io.*;
import java.util.*;

public class Person {
    private int age;    
  
    public Person(int initialAge) {
        // Add some more code to run some checks on initialAge
          
          if (initialAge > 0) {
                age = initialAge;
            } else {
                System.out.println("Age is not valid, setting age to 0.");
                age = 0;
            }
    }

    public void amIOld() {
        // Write code determining if this person's age is old and print the correct statement:
        String output="";
        if (age < 13) {
            output="You are young.";
        }else if (age < 18) {
            output="You are a teenager.";
        }else {
            output="You are old.";
        }
        System.out.println(output);
    }

    public void yearPasses() {
        // Increment this person's age.
          age++;
    }

    public static void main(String[] args) {
