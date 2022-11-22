# An operator that is straightforward, when applied to any boolean expression
# it reverses the boolean value.

# A True statement with an applied not operator turns it into a False statement.

# The not operator is added at the very beginning of the statement.

firstStatement = not 1 + 1 == 2
print(firstStatement)

secondStatement = not 7 < 0
print(secondStatement)

thirdStatement = not (4 + 5 <= 9)
print(thirdStatement)

fourthStatement = not (8 * 2) != 20 - 4
print(fourthStatement)

# Returning to a previous if statement, we're adding several checks using and and not statements

credits = 120
gpa = 1.8

if not credits >= 120:
    print("You do not have enough credits to graduate!")

if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate!")

if not (credits >= 120) and not (gpa >= 2.0):
    print("You do not meet either requirement to graduate!")
    