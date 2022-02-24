"""
Assignment #1: Problem #2
Athena Leong 1/28/2022
Section 04
LeongAthena_assign1_problem2
"""
# given variables
test_score_1 = 97
test_score_2 = 82
test_score_3 = 85

student_first_name = "Grace"
student_last_name = "Hopper"

bonus_points = 2

class_name = "'Introduction to Computer Programming' (no prior experience)"

# print banner for class_name
print("************************************************************")
print(class_name)
print("************************************************************")
# line break
print()
#student name, lname then fname
print("Student: ", student_last_name, ", ", student_first_name, sep="")
# list test scores
print("Most recent test scores: ", test_score_1, ", ", test_score_2, " and ", test_score_3, sep="")
# calculate average score
total = test_score_1 + test_score_2 + test_score_3
average = total / 3
print("Average score:", average)
# display class bonus points
print("Class bonus points:", bonus_points)
# calculate average + bonus
final_score = average + bonus_points
print("Average score with bonus points added:", final_score)
