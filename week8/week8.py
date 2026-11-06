# def get_grade(mark):
#     """Returns the letter grade for a given exam mark."""
#     if mark >= 90:
#         return 'A'
#     elif mark >= 80:
#         return 'B'
#     elif mark >= 70:
#         return 'C'
#     elif mark >= 60:
#         return 'D'
#     else:
#         return 'F'
#
# # Test the function with various marks
# test_marks = [95, 90, 85, 80, 79.99999, 70, 65, 60, 59.9, 42]
#
# print("Mark -> Grade")
# print("-" * 15)
# for m in test_marks:
#     print(f"{m} -> {get_grade(m)}")

# def draw_bar(t, height):
#     """Get turtle t to draw one bar with conditional coloring."""
#     # Determine color based on height
#     if height >= 200:
#         t.fillcolor("red")
#     elif height >= 100:
#         t.fillcolor("yellow")
#     else:
#         t.fillcolor("green")
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write("  " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.forward(10)

# import turtle
#
#
# def draw_bar(t, height):
#     """Get turtle t to draw one bar with color rules and negative value handling."""
#     # 1. Determine color
#     if height >= 200:
#         t.fillcolor("red")
#     elif height >= 100:
#         t.fillcolor("yellow")
#     else:
#         t.fillcolor("green")
#
#     t.begin_fill()
#     t.left(90)
#
#     # 2. Handle text placement for negative vs positive values
#     if height < 0:
#         # For negative bars, write the text at the 0-axis (base) before going down
#         t.write("  " + str(height))
#         t.forward(height)  # moves downward because height is negative
#     else:
#         t.forward(height)
#         t.write("  " + str(height))
#
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)  # returns the turtle back to the baseline (0-axis)
#     t.left(90)
#     t.end_fill()
#     t.forward(10)  # gap
#
#
# # Setup screen and turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.pensize(3)
#
# # Test data including negative values and various thresholds
# data = [48, 117, 200, 240, -50, 75, 150, -20]
#
# tess.penup()
# tess.goto(-200, 0)  # Position turtle to start drawing
# tess.pendown()
#
# for val in data:
#     draw_bar(tess, val)

# wn.mainloop()



#
# import math
#
# def findHypot(x,y):
#     hypot = (x**2 + y**2)**0.5
#     return hypot
#
# def calcWithmath(a , b):
#     hypot = math.sqrt(a**2 + b**2)
#     return hypot
#
# print(findHypot(5 , 12))
# print(calcWithmath(5 , 12))
