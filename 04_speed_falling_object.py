'''User input and calculation'''
print()
import math
print('Welcome to the velocity calculator. Please enter the following:')
print()
mass = float(input('Mass (in kg): '))
gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
time = float(input('Time (in seconds): '))
density = float(input('Density of the fluid (in kg/m^3, 1.3, for air, 1000 for water): '))
density_area = float(input('Cross sectional area (in m^2): '))
drag_constant = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))
print()
little_c = (.5 * density * density_area * drag_constant)
print(f'The inner value of c is: {little_c:.3f}')
velocity = math.sqrt((mass * gravity) / little_c) * (1-math.exp(-1 * ((math.sqrt(mass * gravity * little_c) / mass) * time)))
print(f'The velocity after 10.0 seconds is: {velocity:.3f} m/s')
print()