# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Program 2c
# Date:        8/31/2020

import numpy
import matplotlib

from math import *

x1 = int(input("Enter x1:"))
y1 = int(input("Enter y1:"))
z1 = int(input("Enter z1:"))
t1 = int(input("Enter t1:"))

x2 = int(input("Enter x2:"))
y2 = int(input("Enter y2:"))
z2 = int(input("Enter z2:"))
t2 = int(input("Enter t2:"))

t0 = int(input("Enter Start of Interpolation:"))
t_end = int(input("Enter End of Interpolation:"))
t_avg = (t_end - t0)/4

x0 = x1 + ((x2-x1)/(t2-t1))*(t0-t1)
y0 = y1 + ((y2-y1)/(t2-t1))*(t0-t1)
z0 = z1 + ((z2-z1)/(t2-t1))*(t0-t1)
print("Time of Interest =",t0)
print("x0 =",x0)
print("y0 =",y0)
print("z0 =",z0)

t0 += t_avg

x0 = x1 + ((x2-x1)/(t2-t1))*(t0-t1)
y0 = y1 + ((y2-y1)/(t2-t1))*(t0-t1)
z0 = z1 + ((z2-z1)/(t2-t1))*(t0-t1)
print("----------------------")
print("Time of Interest =",t0)
print("x0 =",x0)
print("y0 =",y0)
print("z0 =",z0)

t0 += t_avg

x0 = x1 + ((x2-x1)/(t2-t1))*(t0-t1)
y0 = y1 + ((y2-y1)/(t2-t1))*(t0-t1)
z0 = z1 + ((z2-z1)/(t2-t1))*(t0-t1)
print("----------------------")
print("Time of Interest =",t0)
print("x0 =",x0)
print("y0 =",y0)
print("z0 =",z0)

t0 += t_avg

x0 = x1 + ((x2-x1)/(t2-t1))*(t0-t1)
y0 = y1 + ((y2-y1)/(t2-t1))*(t0-t1)
z0 = z1 + ((z2-z1)/(t2-t1))*(t0-t1)
print("----------------------")
print("Time of Interest =",t0)
print("x0 =",x0)
print("y0 =",y0)
print("z0 =",z0)

t0 += t_avg

x0 = x1 + ((x2-x1)/(t2-t1))*(t0-t1)
y0 = y1 + ((y2-y1)/(t2-t1))*(t0-t1)
z0 = z1 + ((z2-z1)/(t2-t1))*(t0-t1)
print("----------------------")
print("Time of Interest =",t0)
print("x0 =",x0)
print("y0 =",y0)
print("z0 =",z0)