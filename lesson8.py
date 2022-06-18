#!/usr/bin/python

#tabs \t
print("Monday\tTuesday\tWednesday\tThursday\tFriday\t")
#newline \n
print("Kisumu\nNairobi\nMombasa\n")
#!/usr/bin/python

#################################

#      Dictionaries
#      Name : Collins Muli
#      Date : 17/06/2003 
##################################


# Initializing dictionaries
student = {"Name" : "Collins" , "age" : 22 , "gender" : "Male" , "hobbie" : "reading"}
print(student["Name"])
print(student["age"])
print(student["gender"])
print(student["hobbie"])
student ["ID-No"] = "26401607"
student ["Club"] = "Man-Utd"
print(student)

#Starting with an empty dictionary

student = {}
student["fav-food"] = "cicken wings"
student["home_city"] = "Nairobi"
student["fav_song"] = "Stocks"
print(student)

#Modifying the values in a dictionary
student["Name"] = "Amelia"
student["age"] = 20
print(student)

#Removing key values from a dictionary
del student["fav-food"]
print(student)


#Returning  dictionary from a function
def create_full_name(first_name,second_name):
    person = {'first':first_name, 'second':second_name}
    return person
print(create_full_name("Collins","Muli"))