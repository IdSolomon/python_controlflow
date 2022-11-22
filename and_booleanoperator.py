# and combines two boolean expressions and evaluates as True 
# if both its components are True, but False otherwise.

# Here are some freshly squeezed AND statements --

firstStatement = (1 + 1 == 2) and (2 + 2 == 4)
print(firstStatement)

secondStatement = (1 > 9) and (5 != 6)
print(secondStatement)

thirdStatement = (1 + 1 == 2) and (2 < 1)
print(thirdStatement)

fourthStatement = (0 == 10) and (1 + 1 == 1)
print(fourthStatement)

# Here are two more AND statements --

fifthStatement = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(fifthStatement)

sixthStatement = (4 * 2 <= 8) and (7 - 1 == 6)
print(sixthStatement)

# Here's one exercise with an if statement that checks to see if a student meets both requirements
# using an and statement

credits = 120
gpa = 3.4

if (credits >= 120) and (gpa >= 2.0):
    print("You meet the requirements to graduate!")
    