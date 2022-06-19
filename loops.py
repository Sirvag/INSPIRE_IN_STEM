#!/usr/bin/python/deskop/inspire with stem/loops.py

#######       loops
#       Name : Collins muli
#       Date : 18/6/2022
######################################

#loop
school=['Joy','Hope','Mercy','Happy']
pupil = ['Peace','Patience','Amani','Character']
#hard way
# print(pupil[0],school[0], )
# print(pupil[1] ,school[1] , ) 
# print(pupil[2],school[2] , )
# print(pupil[3], school[3] ,)

for pupil in pupil: 
    print(f'Hello I am pupil {pupil}')



#for loop
for number in range(0,9):
      print(number)

#squares of the number

# for number in range(0,9):
#     print(number**2)

square = number**2
print("number\tSquare")
print("______________________")
for number in range(0,9):
    print(number,"\t",number**2)   



#while loop
colours = ["red", "green" , "blue" , "purple"]

# for colours in colours:
#     if (colours =='red'):
#         print(colours.upper())

i=0
while i < len(colours):
    if(colours[1]=='green'):
        print(colours[1].upper())
        i=i+ 1