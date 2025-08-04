import time

start_number = input("Enter a start number: ")
message = input("Enter your final messages: ")
#print(type(start_number))

# For loop
if start_number.isdigit() and int(start_number) > 0:
    for i in range(int(start_number), 0, -1):
        print(i)
        time.sleep(1)
    print(message)
else:
    print("Please enter a positive integer.")

## For while loop
# current_number = int(start_number)
#
# while current_number >= 1:
#     print(current_number)
#     time.sleep(1)
#     current_number -= 1
#
# print("Enter your final message: Go! ")


'''
Explanation:

import time: This line imports the time module, which provides the sleep() function.

time.sleep(1): This function pauses the program execution for the specified number of seconds (in this case, 1 second).

for i in range(start_number, 0, -1):
    range() generates a sequence of numbers.
    start_number: The starting value of the countdown.
    0: The loop will stop when the number reaches 1 (it does not include the end value in range()).
    -1: This indicates a step of -1, meaning the numbers will decrease by 1 in each iteration.

while current_number >= 1: The while loop continues as long as current_number is greater than or equal to 1.

current_number -= 1: This decrements current_number by 1 in each iteration of the while loop.
'''
