print("My first statement in VS")

# Data is stored in a variable
# variable stores the data in memory
name = "Liesl"

# we don't need to assign the type to the variable

# calculate the tax
income = 10000
tax_percent = 0.2
tax = income * tax_percent
print(tax)

# to reverse
name1 = "Jennifer"

# splicing name1
print("This is Jennifier from 2 to 3 index" +name1[2:4])

# splicing with a step
print("This is Jennifier from 0 to the last index " + name1[0:len(name1):2])


print(name[::-1])

# creating a funciton
def actual_income():
    actual = income - tax
    return actual

print(actual_income())

# Strings are immutable
sentence = "The quick brown fox jumped over the lazy dogs"

# making it into upper, title
print(sentence.upper())

print(sentence.title())

# splitting a time
x = "280422T09:37:00"

date = x.split('T')

print(date[1])

# formating a string
# 1. Traditions
first = "Liesl"
last = "Vellara"
print("This is the stardard way to concatonate my name " + first + " " + last)
# 2. with the format method
print("Using format for {} {} is easier than concatonate".format(first, last))
# 3. next jen method
print(f'This is the easiest to add my name {first} {last}')

# Formatting a floating point number
number = 2.5444444
# rounding to 2 decimal places
print("Changing the number to two decimal places {:.2f}".format(number))

subjects = ["math", "physic", "chemistry"]
print(subjects)
subjects[1] = "geography"
print(subjects)
extra = ['computer', 'PE', 'home science']
total_sub = subjects + extra

# printing the total sub
print("The total number of subjects in the course are: " + str(total_sub))

# appending an element
new = "SUPW"
total_sub.append(new)
print(total_sub)

# inserting in a specific index
degree = "Structural Analysis"
total_sub.insert(1, degree)
print(total_sub)

#removing supw
total_sub.remove("SUPW")
print(total_sub)

# removing the last element
total_sub.pop()
print(total_sub)