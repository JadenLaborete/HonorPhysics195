from math import *

class Club:
    def __init__(self, name, angle, velocity):
        """
        makes instances for different types of golf clubs
        :param name:
        :param angle:
        :param velocity:
        """
        self.name = name
        self.angle = angle
        self.velocity = velocity

    def vix(self):
        """
        :return te velocity intial in x direction:
        """
        return self.velocity * cos(radians(self.angle))

    def viy(self):
        """
        :return te velocity intial in y direction:
        """
        return self.velocity * sin(radians(self.angle))

    def time_solver(self, yi):
        """
        basiclly the quadratic formula, solves the time in displacement equation
        :param yi:
        :return time:
        """
        # d = vit + 0.5(at^2)
        a = -4.9  # acceleration due to gravity
        viy = self.viy()  # calculate initial velocity in y-direction
        discriminant = viy ** 2 - 4 * a * yi

        if discriminant < 0:
            return None  # no real roots

        root1 = (-viy + sqrt(discriminant)) / (2 * a)
        root2 = (-viy - sqrt(discriminant)) / (2 * a)

        # Choose the positive root as the time of flight
        time_of_flight = max(root1, root2)
        return time_of_flight



