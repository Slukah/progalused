"""Set of different math expressions and exe"""

import math

num_a = 5
num_b = 2

# 1. Sum and difference

sum = num_a + num_b

print(f"{num_a} + {num_b} = {sum}")

difference = num_a - num_b

print(f"{num_a} - {num_b} = {difference}")

# 2. Float division

division = num_a / num_b

print(f"{num_a} / {num_b} = {division}")

# 3. Integer division

division = num_a // num_b

print(f"{num_a} // {num_b} = {division}")

# 4. Powerful operations

multiply_numbers = num_a * num_b
power = num_a ** num_b
remainder = num_a % num_b

print(f"{num_a} * {num_b} = {multiply_numbers}")
print(f"{num_a} ** {num_b} = {power}")
print(f"{num_a} % {num_b} = {remainder}")

# 5. Find average

average = (num_a + num_b) / 2
print(f"[{num_a} + {num_b}] / 2 = {average}")

# 6.Area of a circle

radius = 5

circle_area = round(math.pi * radius ** 2)

print(f"{math.pi} * {radius} ** {2}= {circle_area}")

# 7. Area of an equilateral triangle

side_length = num_a

triangle_area = round((side_length ** 2) / 2)

print(f"{side_length} ** {2} / 2 = {triangle_area}")

# 8. Calculate discriminant
num_c = -4
discriminant = num_b ** 2 - 4 * num_a * num_c

print(f"{num_b} ** {2} - 4 * {num_a} * {num_c} = {discriminant}")

# 9. calculate hypotenuse length

num_c = math.sqrt(num_a ** 2 + num_b ** 2)

print(f"{num_c}")

# 10. Calculate hypotenuse length

num_c = 10

num_a = 6

num_b = math.sqrt(num_c ** 2 - num_a ** 2)

print(f"{num_b}")

# 11. Time converter

seconds = 3600

minutes = seconds // 60

hours = minutes // 60

print(f"{seconds}")

print(f"{minutes}")

print(f"{hours}")

# 12. Student helper

angle = 45
sine = math.sin(angle)
cosine = math.cos(angle)

sine = round(sine, 1)
cosine = round(cosine, 1)

print(f"{sine}")
print(f"{cosine}")

# 13. Greetings

num_n = 4

lots_of_heys = num_n * "Hey"

print(f"{lots_of_heys}")

# 14. Adding numbers

num_a = 5

num_b = 2

string_numbers = str(num_a) + str(num_b)

print(f"{string_numbers}")

