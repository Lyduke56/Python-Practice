# Day 2 of 30
# Variables and Built-in Functions

"""
print("Day 2 of Python Practice")

print("print text")                         # print("x"), prints text/values
print(len('text length'))                   # len('x'), length of text,values
print(type('what type'))                    # type('x'), shows data type
print(str(10))                              # str(x), converts number to string
print(int('10'))                            # int('x'), converts to number
print(float(10))                            # float('x'), integer to float
input('Unsay name nimo cuh:')               # input('x'), takes user input

help('keywords')                          # lists all reserved keywords
help(str)                                   # info about string
dir(str)                                    # info about string
"""

# Variable Declaration
first_name = 'Lyduke'
country = 'Philippines'
city = 'Lapu-Lapu'
age = 67
is_married = False
skills = ['JS', 'HTML/CCSS', 'C#', 'Python']
person_info ={
    'firstname' : 'Lyduke',
    'country' : 'Philippines',
    'city' : 'Lapu-Lapu'
}

print('First name:', first_name)
print('First name length:', len(first_name))
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Married:", is_married)
print('Skills:', skills)
print('Person Information:', person_info)

user_name, fave_manga, fave_singer, fave_artist = 'Lyduke56', 'Chainsaw Main', 'Ado', "Liduke/ASK"
print(user_name, fave_artist, fave_manga, fave_singer)