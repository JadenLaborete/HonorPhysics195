from math import sqrt

# Constants
g = 9.81
G = 6.67e-11
m_Earth = 5.98e24  # Mass of the Earth (kg)
r_Earth = 6.38e6  # Radius of the Earth (m)


def v_final1(y):
    """
        Calculates the final velocity of an object in free fall.

        This function computes the final velocity of an object in free fall using the formula:
            v_final1 = sqrt(2 * g * y)
        where 'g' is the acceleration due to gravity and 'y' is the height from which the object falls.

        :param y: A numerical value representing the height from which the object falls (in meters).
        :return: The final velocity of the object (in meters per second).
        """
    return sqrt(2 * g * y)


def v_final2(y):
    """
    Calculates the final velocity of an object in an orbit.

    This function computes the final velocity of an object in a circular orbit using the formula:
        v_final2 = sqrt(2 * G * m_Earth * (1 / r_Earth - 1 / r_initial))
    where 'G' is the gravitational constant, 'm_Earth' is the mass of the Earth, 'r_Earth' is the radius of the Earth,
    and 'r_initial' is the initial distance of the object from the center of the Earth, which is the sum of
    the Earth's radius and the height from which the object is launched.

    :param y: A numerical value representing the height from which the object is launched (in meters).
    :return: The final velocity of the object in orbit (in meters per second).
    """
    r_initial = r_Earth + y
    v_final = sqrt(2 * G * m_Earth * (1 / r_Earth - 1 / r_initial))
    return v_final



def deviation_calc(y):
    """
    Calculates the deviation between two final velocity values.

    This function calculates the deviation between two final velocity values, obtained from functions
    v_final1 and v_final2, as a percentage of the second final velocity.

    :param y: A numerical value representing a parameter for calculating final velocities.
    :return: The deviation between the two final velocity values as a percentage.
    """
    return (abs(v_final1(y) - v_final2(y)) / v_final2(y)) * 100



#Binary search
def find_m(thresholds):
    """
    Finds the value of 'meters' for given deviation thresholds.

    This function iterates through a list of deviation thresholds and determines the corresponding value of meters
    that satisfies each threshold. meters is found using binary search within a predefined range.

    :param thresholds: A list of deviation thresholds for which corresponding 'm' values need to be determined.
                       Each threshold should be a numerical value.

    :return: A dictionary where keys are the deviation thresholds and values are the corresponding 'm' values
             satisfying each threshold.
    """
    y_values = {}
    left = 1
    right = 1e7
    for threshold in thresholds:
        while left < right:
            mid = (left + right) // 2
            deviation = deviation_calc(mid)
            if deviation >= threshold:
                right = mid
            else:
                left = mid + 1
        y_values[threshold] = left
        left = 1
        right = 1e7
    return y_values




def main():
    """
       Executes the main functionality of the program.

       This function calculates and prints various parameters based on deviation thresholds.
       It calls the 'find_m' function to determine the minimum height for each deviation threshold,
       and then calculates final velocities using 'deviation_calc', 'v_final1', and 'v_final2' functions.
       Finally, it prints the results including minimum height, final velocities, and the deviation threshold.

       :return: None
       """
    thresholds = [1, 5, 10, 25]
    y_values = find_m(thresholds)
    for threshold, y in y_values.items():
        v1_final = v_final1(y)
        v2_final = v_final2(y)
        print(f"For deviation less than or equal to {threshold}%:")
        print(f"  Height : {y} meters")
        print(f"  v_final1: {v1_final:.2f} m/s")
        print(f"  v_final2: {v2_final:.2f} m/s")
        print()


if __name__ == "__main__":
    main()
