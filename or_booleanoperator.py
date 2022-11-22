# The boolean operator OR combines two expressions into a larger expression 
# that is True if either component is True.

# If an or statement has two True components, it is also True.

# Here are some freshly baked OR statements --

firstStatement = True or (3 + 4 == 7)
print(firstStatement)

secondStatement = (1 - 1 == 0) or False
print(secondStatement)

thirdStatement = (2 < 0) or True
print(thirdStatement)

fourthStatement = (3 == 8) or (3 > 4)
print(fourthStatement)

# The following boolean expressions are baked just for you!

fifthStatement = (2 - 1 > 3) or (-5 * 2 == -10)
print(fifthStatement)

sixthStatement = (9 + 5 <= 15) or (7 != 4 + 3)
print(sixthStatement)

# The following baked if statement checks if a student either has 120 or more credits
# or a GPA 2.0 or higher --

credits = 118
gpa = 2.0

if (credits >= 120) or (gpa >= 2.0):
  print("You have met at least one of the requirements.")
  