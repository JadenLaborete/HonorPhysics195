import math


def calculate_horizontal_distance(H_m, distance_m, incline_angle_deg=30):
    # Convert incline angle to radians
    incline_angle_rad = math.radians(incline_angle_deg)

    # Calculate horizontal distance from the launch point to the target
    x_m = (distance_m - H_m / math.tan(incline_angle_rad)) * math.cos(incline_angle_rad)

    return x_m


def calculate_position_on_incline(x_m, incline_angle_deg=30):
    # Convert incline angle to radians
    incline_angle_rad = math.radians(incline_angle_deg)

    # Calculate position on the incline
    position_on_incline = x_m / math.cos(incline_angle_rad)

    return position_on_incline


# Given values
H_m = 0.01  # Height of target above the ground (m)
distance_m = 0.40  # Distance to target (m)
r_m = 0.892  # Height of launch point above ground (m)

# Calculate horizontal distance
x_m = calculate_horizontal_distance(H_m, distance_m)

# Calculate position on the incline
position_on_incline_m = calculate_position_on_incline(x_m)
print("Place the ball on the incline at:", round(position_on_incline_m, 2), "m from the launch point")

#each 10cm past 50cm add 5cm
#.5cm for each cm at past 50