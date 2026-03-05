import math

# Get input and convert to a list when a white space is seen
x_input = input().split()

# Get full raduis and raduis of the crust as integers
r = int(x_input[0])
c = int(x_input[1])

# Get the area of full pizza with crust
r_percent = math.pi * r**2

# New Raduis of Pizza without crust
t = r-c
# Area without crust
t_percent = math.pi * t**2

# Percentage of pizza without crust
without_crust_percent = (t_percent / r_percent) * 100

print(without_crust_percent)
