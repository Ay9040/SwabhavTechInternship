student_tuple = ("sha",[10,20,30])
print(student_tuple[1][0])
print(id(student_tuple))
student_tuple[1][0] = 100
print(student_tuple)
print(id(student_tuple))