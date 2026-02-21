# Single Line String
letter = 'x'
sentence = 'single line string'

# Multi-line String
multi_line = '''this is a 
multi
line
string.'''

# String Concatenation
first = 'i am '
second = 'concatenating '
third = 'it uoghh.'

ong = first + second + third
print(ong)

# Old Style String Formatting (%)
# %s, %f, %.xf, %d
old_string = "test"
old_character = 'x'
old_integer = 5
old_float = 2.35

print("%s %s %f %.1f %d" %(old_character, old_string, old_float, old_float, old_integer))

# New Style ('{}'. format)
new_string = "new test"
new_character = "n"
new_integer = 10
new_float = 1.67

print('{} {} {} {:.1f}'.format(new_string, new_character, new_integer, new_float))

# String Interpolation
a = 4
b = 3
print(f'{a} + {b} = {a +b}')

# String as Sequence of Characters
language = 'TeSt'
a,b,c,d = language # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)

# by Index
print(language[0])
print(language[-4])
