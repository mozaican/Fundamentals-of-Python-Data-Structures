"""
A standard science experiment is to drop a ball and see how high it bounces. 
Once the "bounciness" of the ball has been determined, the ratio gives a
bounciness index. For example, if a ball dropped from a height of 10 feet
bounces 6 feet high, the index is 0.6 and the total distance traveled by the
ball is 16 feet after one bounce. If the ball were to continue bouncing, the
distance after two bounces would be 10 ft + 6 ft + 6 ft + 3.6 ft = 25.6 ft.
Note that distance traveled for each successive bounce is the distance to the 
floor plus 0.6 of that distance as the ball comes back up. Write a program
that lets the user enter the initial height of the ball and the number of
times the ball is allowed to continue bouncing. Output should be the total
distance traveled by the ball.  
"""

class Ball:
    def __init__(self, initial_height, number_of_bounces):
        self.initial_height = initial_height
        self.number_of_bounces = number_of_bounces
        self.bounce_height = self.initial_height - 4 
        self.index_of_bounciness = self.bounce_height / self.initial_height
        self.total_distance = self.initial_height + self.bounce_height

    def calculate_total_distance(self):
        for i in range(0, self.number_of_bounces - 1): 
            self.total_distance += self.bounce_height + (self.index_of_bounciness * self.bounce_height)
            self.bounce_height *= self.index_of_bounciness
        return self.total_distance


if __name__ == '__main__':
    initial_height = input("Enter the initial height of the ball: ")
    number_of_bounces = input("Enter the number of bounces: ")
    ball = Ball(int(initial_height), int(number_of_bounces))
    print("The total distance traveled by the ball is", ball.calculate_total_distance())