# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over"
# group.

lab_group = 24
students_1=113
students_2=175
students_3=12

std_group_1=int(students_1/lab_group)
std_group_2=int(students_2/lab_group)
std_group_3=int(students_3/lab_group)

small_std_1= students_1 - (std_group_1 * 24)
small_std_2= students_2 - (std_group_2 * 24)
small_std_3= students_3 - (std_group_3 * 24)


print('For 113 studnets:  ')
print(f'Full Groups: {std_group_1} ')
print(f'Smaller Group students: {small_std_1} ')
print('')

print('For 175 studnets:  ')
print(f'Full Groups: {std_group_2} ')
print(f'Smaller Group students: {small_std_2} ')
print('')


print('For 12 studnets:  ')
print(f'Full Groups: {std_group_3} ')
print(f'Smaller Group students: {small_std_3} ')
print('')

