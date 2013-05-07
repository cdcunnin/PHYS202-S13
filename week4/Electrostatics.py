import numpy as np

def dipolePotential(x,y,q1,q2,d):
    """This takes the charges and distance between two particles""" 
    #and gives you the potential at an x-y point.
    k = 8.99*(10**9)
    P = ((k*q1)/((x**2) + (y - d)**2)**1/2) - ((k*q2)/((x**2) + (y + d)**2)**1/2)
    return P

def pointPotential(x,y,q,posx,posy):
    """This will take the x-y position of a particle and its charge""" 
    #and spit out the potential at a point x,y from the particle.
    x=x-posx
    y=y-posy
    k = 8.99*(10**9)
    V = ((k*q)/((x**2) + (y**2))**1/2)
    return V

def quadPotential(x,y,q1,q2,q3,q4,d):
	k = 8.99*(10**9)
	Q = ((k*q1)/((x**2) + (y - d)**2)**1/2) - ((k*q2)/((x**2) + (y + d)**2)**1/2)
	return Q

