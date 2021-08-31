import math
#Square area function
def area_square_function(square_side):
    square_area = square_side * square_side
    return square_area

#Rectangle area function
def area_rectangle_function(rec_length, rec_width):
    rec_area = rec_length * rec_width
    return rec_area

#Circle area function
def area_circle_function(circle_radius):
    circle_area = math.pi * circle_radius * circle_radius
    return circle_area

#User input to determine shape
print()
print('AREA COMPUTATION PROGRAM')
shape_type = input('What type of shape do you have? [SQUARE, RECTANGLE, CIRCLE]: ')
#Square
if shape_type.upper() == 'SQUARE':
    square_side = int(input('What is the length of one of the sides? : '))
    square_area = area_square_function(square_side)
    print(f'The area of the square is {square_area:.2f}')
#Rectangle
elif shape_type.upper() == 'RECTANGLE':
    rec_length = int(input('What is the length of one of the rectangles sides? : '))
    rec_width = int(input('What is the width of one of the rectangles sides? : '))
    rec_area = area_rectangle_function(rec_length, rec_width)
    print(f'The area of the rectangle is {rec_area:.2f}')
#Circle
elif shape_type.upper() == 'CIRCLE':
    circle_radius = int(input('What is the radius of the circle? : '))
    circle_area = area_circle_function(circle_radius)
    print(f'The area of the circle is {circle_area:.2f}')






