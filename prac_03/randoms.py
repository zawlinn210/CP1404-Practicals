import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
Ans: A random integer number from 5 to 20 is generated. (9) 
What was the smallest number you could have seen, what was the largest?
Ans: 5 and 20

What did you see on line 2?
Ans: A random integer number from 3 to 10 with a difference of 2 is generated. (7)
What was the smallest number you could have seen, what was the largest?
Ans: 3 and 9
Could line 2 have produced a 4?
Ans: No, it couldn't.

What did you see on line 3?
Ans: A random float number from 2.5 to 5.5 is generated. (2.6010299194767197)
What was the smallest number you could have seen, what was the largest?
Ans: 2.5 and 5.5

"""
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
