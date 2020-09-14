# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Formula Scavenger Hunt 2.0
# Date:        8/30/2020

import numpy
import matplotlib

from math import *

name_UIN = "Luca Maddaleni, 330001030"
print(name_UIN)
about_me = "I was born and raised in Atlanta, Georgia, and before I moved in I had only been in Texas once."
print(about_me)
resistance = 20
current = 5
voltage = resistance * current
print(voltage) # Took physics in HS, already knew Ohm's law (V=IR)
mass = 100
velocity = 21
kinetic_energy = 0.5 * mass * velocity**2
print(kinetic_energy) # chem.wisc.edu, needed a refresher on this formula
fluid_velocity = 100
viscosity = 1.2
linear_dimension = 2.5
reynolds_number = (fluid_velocity*linear_dimension)/viscosity
print(reynolds_number) # airfoiltools.com
sb_constant = 5.67*10**-8
temperature = 2200
energy_radiated = sb_constant * temperature**4
print(energy_radiated) # http://hyperphysics.phy-astr.gsu.edu/ Fun Fact: my dad recently graduated from GSU with a law degree
normal_stress = 20
cohesion = 2
friction_angle = 35
shear_stress = cohesion + normal_stress*(tan(friction_angle))
print(shear_stress) # https://www.slideshare.net/1mirfan/geotechnical-engineeringii-lec-2-mohrcoulomb-failure-criteria
