# area of a circle

r = input(" enter the radius of circle ")
print(r)
pi = 3.142
area = int (r) * int(r) * pi
print("   area of the circle is " + str(area)) 

#volume of a cylinder

r = input(" enter radius of cylinder ")
print(r)
h = input(" enter the height ")
print(h)
pi = 3.142
ba = pi * int(r) * int(r)
vol = ba * int(h)
print("   volume of the cylinder is " + str(vol))


#volume of a cube

l = input(" enter length ")
print(l)
vol = int(l) * int(l) * int(l)
print("   volume of the cube is " + str(vol) )

#surface area of a cylinder

r = input(" enter radius of cylinder ")
print(r)
pi = 3.142
h = input(" enter height of cylinder ")
print("h")
both = 2
d = int(r) * both
curved_surface = d * pi * int(h)
circle_area = pi * int(r) * both
surface_area = circle_area + curved_surface
print("   surface area of the cylinder is " + str(surface_area))