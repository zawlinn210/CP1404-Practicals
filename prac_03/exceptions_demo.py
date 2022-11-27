"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: It occurs when function receives an argument with right data type but an invalid number.
2. When will a ZeroDivisionError occur?
Ans: It occurs when a number is divided by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans: Yes. By using the if statement and try/expect statement.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Another code that uses if statement
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
if denominator != 0:
    fraction = numerator / denominator
    print(fraction)
else:
    print("Cannot divide by zero1")