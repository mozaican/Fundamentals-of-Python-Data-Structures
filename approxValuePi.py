"""
The German mathematician Gottfried Leibniz developed the following
method to approximate the value of pi: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
Write a program that allows the user to specify the number of
iterations used in this approximation and displays the resulting value.
"""

def get_value_pi(iterations):
    adding = 0
    for i in range(1, iterations + 1, 2):
        if i % 4 == 1:
            adding += 1/i
        else:
            adding -= 1/i 
    pi = 4 * adding
    return pi

# alternative solution
def get_value_pi(iterations):
    adding = 0
    sign_positive = True
    for i in range(1, iterations + 1, 2):
        if sign_positive:
            adding += 1/i
            sign_positive = False
        else:
            adding -= 1/i
            sign_positive = True 
    pi = 4 * adding
    return pi