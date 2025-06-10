## QUESTION
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Follow up: Could you solve it without converting the integer to a string?

## PROCESS
# 1 - ones
# 2 - tens
# 0 - hundreds
# 2 - thousands
# 1 - ten thousands

# reversed = 0
# reversed = 1
# reversed = 10 + 2 = 12
# reversed = 120 + 0 = 120
# reversed = 1200 + 2 = 1202
# reversed = 12020 + 1 = 12021


x = 121

## Solution 1
reversed = 0
number = x     
while True:
    reversed += number % 10
    number = number // 10

    if number != 0:
        reversed *= 10
    else:
        break


## Solution 2
reversed_num = 0
number = x

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10

print(reversed == x)