#!/usr/bin/python

########      arithmetic progression
#       Name : Collins Muli
#       Date : 27/5/2022
######################################
#a=first_number
#d=steps(commmon diff)
#n=number_of_terms

a=int(input("enter the first number"))
d=int(input("enter the common difference"))
n=int(input("enter the number of terms"))
for i in range (1,n+1):
    n_term=a+(i-1)*d
    print(n_term)
sum_n=(n_term/2)*(2*a+(n-1)*d)
print(sum_n)
