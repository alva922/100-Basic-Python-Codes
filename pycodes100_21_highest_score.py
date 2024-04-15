# https://newdigitals.org/2024/02/24/100-basic-python-codes/#highest-score
# Highest Score
# Calculating the highest student scores from a list of students
# HIGHEST STUDENT SCORES
 
# Example input = 67 82 98 67 82
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
 
# Method 1 - Easy
highest_score = 0
 
for score in student_scores:
    if score > highest_score:
        highest_score = score
 
print(f"The highest score in the class is: {highest_score}")
#Example I/O
Input a list of student scores 22 45 67 82 44
[22, 45, 67, 82, 44]
The highest score in the class is: 82
