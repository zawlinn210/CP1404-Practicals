"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Get score, determine status and generate random number functions"""
    score = float(input("Enter score: "))
    print(determine_score_status(score))
    random_number = generate_random_number()
    print(random_number)
    print(determine_score_status(random_number))


def determine_score_status(score):
    """Determine score status"""
    if score < 0 or score > 100:
        status = "Invalid score"
    elif score >= 90:
        status = "Excellent"
    elif score >= 50:
        status = "Passable"
    else:
        status = "Bad"
    return status


def generate_random_number():
    """Generate random number"""
    number = random.randint(0, 100)
    return number


main()
