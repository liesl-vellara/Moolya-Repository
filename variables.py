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

