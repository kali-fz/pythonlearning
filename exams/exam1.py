# =============================================
#         PYTHON EXAM — Parts 1 to 4
# =============================================
# Instructions:
#   - Write your answer below each question.
#   - Run the file to check your output.
#   - Do NOT look at the lesson files!
# =============================================


# --------------------------------------------------
# SECTION 1 — Variables & Print  (Part 1)
# --------------------------------------------------

# Q1. Create two variables, one for your first name and one for your last name.
#     Then print your full name on one line by combining them.


# Q2. Create a variable called 'header' that contains exactly 20 asterisk (*) characters.
#     Print it.


# --------------------------------------------------
# SECTION 2 — Operators & Booleans  (Part 2)
# --------------------------------------------------

# Q3. Create two number variables: a = 15 and b = 4
#     Print the result of:
#       a) a divided by b              (regular division)
#       b) a floor divided by b        (rounds down)
#       c) a to the power of b


# Q4. Using the variables below, predict what each print() will output,
#     then uncomment the lines and run to check.
import math
x = True
y = False
z = True

# print(x and y)
# print(y or z)
# print(x and z)
# print(y and x)   # remember: stops at the first False


# Q5. Without running the code first, write a comment next to each line
#     saying whether the result is True or False.
print(10 == 10)     # ?
print(10 != 5)      # ?
print(7 > 10)       # ?


# --------------------------------------------------
# SECTION 3 — If / Else & Ternary  (Part 3)
# --------------------------------------------------

# Q6. Write an if/else statement:
#     If a number variable called 'score' is greater than or equal to 50,
#     print "Pass", otherwise print "Fail".
#     Test it with score = 72 and score = 30.
score = 72


# Q7. Rewrite Q6 using a ternary (one-line) operator.


# --------------------------------------------------
# SECTION 4 — Data Types, String Methods & Math  (Part 4)
# --------------------------------------------------

# Q8. Create a string variable with your name.
#     Print it in ALL UPPERCASE, then all lowercase.


# Q9. Using the string "  hello world  " (with leading/trailing spaces),
#     print the string with the spaces removed using a string method.


# Q10. Build this menu output using ljust, rjust, and center:
#
#      ========MENU========
#      Tea.............£1.50
#      Cake............£2.00
#      Sandwich........£3.50
#
# Hint: total width = 20


# Q11. Cast the string "2026" to an integer, add 4 to it, and print the result.


# Q12. Use the math module to:
#      a) Print the square root of 144
#      b) Round 7.3 UP to the nearest whole number  (math.ceil)
#      c) Round 7.9 DOWN to the nearest whole number (math.floor)


# Q13. Create a complex number 3+5j.
#      Print only its real part and only its imaginary part separately.


# =============================================
#  BONUS — put it all together
# =============================================
# Q14. Ask the user for a number using input() and cast it to a float.
#      If it is greater than 100, print "Big number!", otherwise print "Small number."
#      (Hint: float("42.5") works just like int())
