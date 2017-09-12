#Morgan Baughman
#9/11/17
#Slope.py - finding the slope of a line.

x1 = int(input('Enter x1 value: '))
x2 = int(input('Enter x2 value: '))
y1 = int(input('Enter y1 value: '))
y2 = int(input('Enter y2 value: '))
slope = (y2-y1)/(x2-x1)
print('The slope is:' , (y2-y1)/(x2-x1))
print('The equation of the line is: y=' , (slope) , 'x' , y1+slope*x1)
