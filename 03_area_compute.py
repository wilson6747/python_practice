'''Square area input and compute'''
print()
print('This program will compute the area of shapes for you!')
print()
print('Area of a square:')
square_side = input('What is the length of the side of the square? - ')
square_side = int(square_side)
square_area = square_side ** 2
print(f'The area of the square is {square_area}!')
print()

'''Rectangle area input and compute'''
print('Area of a rectangle:')
rect_length = int(input('What is the length of the rectangle? -'))
rect_width = int(input('What is the width of the rectangle? - '))
rect_area = rect_length * rect_width
print(f'The area of the rectangle is {rect_area}!')
print()

'''Circle area input and compute'''
print('Area of a circle:')
circ_radius = int(input('What is the radius of the circle? - '))
circ_area = 3.14 * (circ_radius ** 2)
print(f'The area of the circle is {circ_area}!')
print()
