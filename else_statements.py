# Including a lot of if statements in a function the code becomes
# a little cluttered and messy.

# Thankfully we are saved with else statements that allow
# us to elegantly describe what we want our code to do
# when certain conditions are not met.

# Here's something worthwhile - An else statement in conjunction with an if statement --

credits = 120
gpa = 1.9

if (credits >= 120) or (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")
