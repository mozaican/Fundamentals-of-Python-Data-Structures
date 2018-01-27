"""
The German mathematician Gottfried Leibniz developed the following
method to approximate the value of pi: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
Write a program that allows the user to specify the number of
iterations used in this approximation and displays the resulting value.
"""

from math import pi

def getValuePi(iterations):
    sum = 0
    for i in range(1, iterations + 1, 2):
        if i % 4 == 1:
            sum = sum + 1/i
        else:
            sum = sum - 1/i 
    pi = 4 * sum
    return pi

getValuePi(4)