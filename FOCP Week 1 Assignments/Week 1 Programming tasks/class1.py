group_size=int(input("group"))
class_size=int(input("class"))

full_group=class_size//group_size
left_over=class_size%group_size

print(full_group)
print(left_over)

# print(f"THere will be {full_group} groups with {left_over} students remaining")
# print("THere will be "  +  str(full_group) + " groups with " +  str(left_over) +"  students remaining")

a= {1,2,3,4,5,6,6}
print(a)

# if(left_over>1):
#     print("THere will be "  +  str(full_group) + " group with " +  str(left_over) +"  students remaining")
# else:
#     print("THere will be "  +  str(full_group) + " groups with " +  str(left_over) +"  student remaining")
print(f"There will be {full_group} {'group' if full_group <=1  else 'groups'} with {left_over} {'student' if left_over <= 1 else 'students'} remaining")
    
    
    