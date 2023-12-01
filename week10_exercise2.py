#to check if a number is beautiful or not
def is_the_same(number):
    number = str(number)
    for i in range (0, len(number)):
        if (number[i] != number[i-1]):
            return False
    return True

#user input
x = int(input("Input x: "))
while (x % 2 == 0) or (x % 5 == 0):
    x = int(input("Input x: "))

#loop to check if a number is beautiful or not
#if not, add it with the original number which is the x_copy
x_copy = x
while is_the_same(x) == False:
    x += x_copy

print(f"The smallest beautiful number divisible by {x_copy} is {x}")