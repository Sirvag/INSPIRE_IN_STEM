######       Dictionaries
#       Name : Collins Muli
#       Date : 20/5/2022
######################################

#Learning about lists 
motorcycle_owner = "Muli"
plate_number =['A1234', 'U1234', 'E1234']
motorcycle = ['honda','yamaha','suzuki']
#print(plate_number)
#print(motorcycle)
print(motorcycle+plate_number)
print(motorcycle)
#print(motorcycle+plate_number)
#accessing list items using index
#print(motorcycle)
motorcycle[1]= "JEEP"
print(motorcycle)
#adding element in a list
#print (motorcycle)
motorcycle[1]= "JEEP"#changing an element in a list
print("I love " + str (motorcycle[1]))
#adding an element to a list
motorcycle.append('JEEP')#ading item into a list
print(motorcycle)
#task---print the motorcycle and their plate number
#deleting an item from a list
del motorcycle [2]
print (motorcycle)
#deleting an item from a list
popped_motorcycle = motorcycle.pop()
print (popped_motorcycle)
#print (popped_motorcycle)
#task print a statement:
#My name is Mangereza and I own a motorcycle plate number
print ('Muli','honda','E1234')
p_statement =  (f"My name is {motorcycle_owner} and I own a {motorcycle[1]} plate number {plate_number[1]}")
print (p_statement)
#removing an item from a list
motorcycle.remove ('JEEP')
print (motorcycle)
