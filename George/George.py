name = "Michal"
age = 23.5
height = 1.91
student_now = True
city = "Poznań"
print(name, " is ", age, " years old ")
print(type(name), type(age))
print(type(height), type(student_now))

slices_per_student = 3
students = 15
present_students = students - 5
total_slices_needed = present_students * slices_per_student
cost_per_student = 500 / present_students
boxes_to_order = (total_slices_needed // 8) + 1
leftover_slices = (boxes_to_order*8)%present_students

print(f"Boxes to order: {boxes_to_order}, Leftover slices: {leftover_slices}, Cost per student: {cost_per_student}")
