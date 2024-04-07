## Question 1
Following is the Taylor approximation for calculating $e^x$. <br>
$e^x \approx 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots + \frac{x^n}{n!} $ <br>

Using Loop structure to write a program that prompts the user for a binary integer to choose the calculating mode (0: **epsilon**, 1: **fixed number of terms**) and calculate $e^x$ based on the chosen mode.<br>
Display your results with 8 digits after decimal point.<br>
- **Epsilon:**
    - prompts the user for a value of x and epsilon
    - The calculation will stop when the absolute value of addend (term to be added to the sum) is less than or equal epsilon
- **Fixed number of terms:** 
    - prompts the user for a value of x and number of terms (n)
    - The calculation will stop after the n terms have been added <br>
Below are some examples concerning number of terms to be added:<br>
$e^x \approx 1 $       if one term is added<br>
$e^x \approx 1 + x + \frac{x^2}{2!}$ if 3 terms are added <br>
$e^x \approx 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} $ if 4 terms are added  etc... <br>
Print the result as in the sample runs, below.<br>
**Note:** you can import factorial function from math library and use it.

## Question 2
Write a program that can generate even or odd parity bit for a given Binary code based on user's choice. Binary code is a code that contains only two possible digits "0" and "1". Parity bit is a bit (0 or 1) added to the left most position of a binary code for error detection purpose. There are two variants of parity bits: even parity and odd parity. 

The program will ask user to enter a Binary Code(any length) followed by a choice of parity type : 'e' for even parity and 'o' for odd parity. The program returns same Binary code with parity bit(0/1) set at the left most bit position of the code. The program must also be able to detect the validity of the input (Binary or Decimal).

Detail steps to follow after validating the input:
1. Count total number of "1" into the given binary Code
2. If the total number of "1" is even and user's choice is "e", add a "0" to the left most position of the binary code and print it
3. If the total number of "1" is even and user's choice is "o", add a "1" to the left most position of the binary code and print it
4. If the total number of "1" is odd and user's choice is "e", add a "1" to the left most position of the binary code and print it
5. If the total number of "1" is odd and user's choice is "o", add a "0" to the left most position of the binary code and print it
