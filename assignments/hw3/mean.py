"""
Name: Hugo Bachaumard
mean.py

Problem: Write a program that uses definite loops to output means.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# Use for loops and arithmetic to get RMS Average, Harmonic Mean and Geometric Mean
# The inputs will be the number of values as well as the values of those numbers.
# The outputs will be the RMS Average, Harmonic Mean and Geometric Mean
# Input the number of values being tested.
# Set the for loop with a range of 1 to the number of Values
# Input the Values in the loop
# Get the mean squared of the values (RMS)
# Add all the values of 1 divided by the value (Harm)
# Get the product of all the values (Geom)
# End Loop
# Divide the mean squared of the values over number of values and get the square root of that (RMS)
# Divide the number of values by the addition of 1 over the values (Harm)
# Take the product of the values and raise it to the power of 1 over the number of values (Geom)
# Print all the values and round them to 3 decimal points.


def main():

    num_values = eval(input("enter the values to be entered:"))
    mean_square = 0
    harmonic_mean = 0
    geo_mean = 1
    for i in range(1, num_values+1):
        values = eval(input("enter value:"))
        mean_square = mean_square + values**2
        harmonic_mean = harmonic_mean + 1/values
        geo_mean = geo_mean * values
    mean_square = mean_square / num_values
    rms_average = mean_square**0.5
    harmonic_mean = num_values / harmonic_mean
    geom_mean = geo_mean ** (1 / num_values)
    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geom_mean, 3))


if __name__ == '__main__':
    main()
