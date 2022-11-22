# BEHOLD!
# Else if statements, or 'elif' statements check another condition
# after the previous if statements conditions are not met.

# We use elif statements to control the order we want our
# program to check each of our conditional statements.

donation = 2000
print("Thank you for the donation!")
 
if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")

# Here's another morsel --

grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")

# So, the if statement is checked, then each elif statement is checked from top 
# to bottom, then finally the else code is executed if none of the previous conditions have been met.