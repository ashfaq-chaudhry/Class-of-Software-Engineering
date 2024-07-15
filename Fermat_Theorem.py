'''Items to include in your opening comment:

a title for your program: Fermat's Last Theorem: The Proof in the Pie!
the name of the file that holds your program: Fermat_Theorem
a list of any external files necessary to run your program: Does not apply (see GitHub)
a list of external files your program creates: Does not apply
the names of any programmers working on the program: Oscar Quiles
email address of all programmers: oscardavidquiles@gmail.com
the course number and section number of the course you’re writing this program for: SU24-CPSC-60500-001 (Software Engineering)
the date you finished the program and submitted it: 07/15/2024
an explanation of what the program does: This program looks for near misses (numbers that are very similar yet different) in the following equation: X^N + Y^N = Z^N.
N represents the power that the user wishes to test and K is the range for X and Y which is between 10 and K.
The program prints the results (nearest miss) based on the user's input.
any resources you used to complete the program: https://math.stackexchange.com/questions/526330/fermats-last-theorem-near-misses
Other comments that are required:
each declaration should include a comment that explains its use
each subprogram (function, subroutine, object,…) should have an opening comment describing its purpose)
each loop should be preceded by a comment that describes its purpose
any statement that is particularly unclear or “tricky” should have a comment clarifying its use to the human reader
What programming language to use? Python
'''


# This method asks the user for their inputs and starts the search for near misses.
def main():

    # This is asking the user what power of n they wish to use. It must be between 3 and 11.
    n = int(input("Please enter a natural number for N. It must be greater than 2 but less than 12: "))
    if n <= 2 or n >= 12:
        print("Check your input. The value of N must be greater than 2 but less than 12.")
        return

    # Asks the user to input the value of K. It must be between 11 and 99.
    k = int(input("Please enter a natural number for K. It must be greater than 10 but less than 100: "))
    if k <= 10 or k >= 100:
        print("Check your input. The value of K must be greater than 10 but less than 100.")
        return

    # Calls the function to find near misses with the users selected n and k
    located_misses(n, k)


'''This method is looking for the near misses in Fermat's last theorem: X^N + Y^N = Z^N
N is the power to test and K is the range for X and Y. This method also prints out results.'''

def located_misses(n, k):


#variable creation
    nearest_miss = None
    small_relative_difference = float('inf')

    # Nested loop through x and y in k's range
    for x in range(10, k + 1):
        for y in range(x, k + 1):
            #Equation for Fermat's Theorem provided in class
            sum_XY = x ** n + y ** n
            z = int(sum_XY ** (1 / n))

            # Calculate the differences
            ZN = z ** n
            Z1N = (z + 1) ** n
            #calculates the absolutue difference
            difference1 = abs(sum_XY - ZN)
            difference2 = abs(Z1N - sum_XY)
            #smallest of the two misses is absoulute difference
            min_difference = min(difference1, difference2)

            # equation for the relative miss
            relative_difference = min_difference / sum_XY

            # details of the near misses
            print(f"X={x}, Y={y}, Z={z} : X^N + Y^N = {sum_XY}, Z^N = {ZN}, (Z+1)^N = {Z1N}, "
                  f"Diff Absolute = {min_difference}, Diff Relative = {relative_difference:.6f}")

            # Refreshes the nearest miss if the current is smaller
            if relative_difference < small_relative_difference:
                small_relative_difference = relative_difference
                nearest_miss = (x, y, z, min_difference, relative_difference)
        #prints results
    if nearest_miss:
        x, y, z, final_difference, relative_difference = nearest_miss
        print(f"\nNearest miss: X={x}, Y={y}, Z={z} with an absolute difference of {final_difference} and a relative difference of {relative_difference:.6f}")

    # Stops the program at users desire
    input("\nIf you dont want to wait for the program to finish then press enter.")

#calls the main method
main()