# A simple function
def math():
    a=75
    b=25
    c = a*b
    return c

#print(math())

# making a function with arguments
def new_math(a,b,c):
    return a + b * c

#print(new_math(7,9,10))
# making a division function
def division(new_num):
    return new_num/2

# using new math method to do some division
complex_math = new_math(7, 9, 10)
print(division(complex_math))


# using an if- else in a function
# the function will check if the numbers are odd or even
list_num = [1,2,4,25,11,30,55]
def odd_or_even(num_list):
    for num in num_list:
        if(num%2 == 0):
            print(f'{num} is even')
        else:
            print(f'{num} is odd')

# we will call the method without the print statement
# this will return the function without "None"
odd_or_even(list_num)
