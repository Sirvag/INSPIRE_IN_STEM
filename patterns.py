#!/usr/bin/python/deskop/inspire with stem/patterns.py

#######       patterns
#       Name : Collins muli
#       Date : 18/6/2022
######################################

rows=int(input("enter number of rows "))
for i in range (rows):
    for j in range (i+1):
        print(j+1,end=" ")
    print("\n")