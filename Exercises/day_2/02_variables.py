# Day 2: 30 Days of Python Programming

first_name = 'lyduke'
last_name = 'kaffe'
full_name = 'tatsuki fujimotor'
country = 'Philippines'
city = 'Lapu-Lapu'
age = '20'
year = '2026'
is_married = False
is_true = False
is_light_on = True

multiple, variable, one_line = 'test', '5', 1

print(first_name, last_name, full_name, country, city, age, year, is_married, is_light_on)
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(type(multiple), type(variable), type(one_line))
print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4

print(num_one + num_two)
diff = (num_one - num_two)
product = (num_one * num_two)
division = (num_one / num_two)
remainder = (num_two / num_one)
exp = (num_one ** num_two)
floor_division = (num_one // num_two)
area_of_circle = (3.14)*(30**2)
circum_of_circle = 2*(3.14)*(30)

print(diff, product, division, remainder, exp, floor_division, area_of_circle, circum_of_circle)

user_input = input("Insert Circle Radius: ")
user_radius = int(user_input)
user_area = (3.14)*(user_radius**2)
print(user_area)

user_name = input("Name:")
user_country = input("Country:")
user_age = input("Age:")

print(user_name, user_country, user_age)