# input by user
# User inputs new number untill a negative number is entered

max_int = 0
num_int = 0

while 1:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int
    if num_int < 0:
        break
print("The maximum is", max_int)
