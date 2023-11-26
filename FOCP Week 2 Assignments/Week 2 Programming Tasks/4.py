# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.

total_sweets=int(input('Enter the total no of sweets: '))
total_pupils=int(input('Enter the total no of pupils: '))

indivisual_sweet=total_sweets//total_pupils
left_sweets=total_sweets%total_pupils

if(indivisual_sweet==0):
    print("Sorry You dont have enough sweets for everyone")
elif(indivisual_sweet>=2):
    print(f"You should give {indivisual_sweet} sweets to each pupil.")
else:
    print(f"You should give {indivisual_sweet} sweet to each pupil.")
    
if(left_sweets==0):
    print("You will have 0 sweet left.")
else:
    print(f"You will have {left_sweets} {'sweets' if left_sweets >1 else 'sweet' } left")