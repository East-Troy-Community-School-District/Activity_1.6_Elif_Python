# Grader
# Pawelski
# 9/29/2024
# Programming Fundamentals

points_earned = int(input("Enter your points you earned on the assignment >> "))
total_points = int(input("Enter the total points you could have earned on the assignment >> "))
percentage = points_earned / total_points * 100
if percentage >= 90:
  print("A")
elif percentage >= 80:
  print("B")
elif percentage >= 70:
  print("C")
elif percentage >= 60:
  print("D")
else:   # Modify this line of code!
  print("F")
