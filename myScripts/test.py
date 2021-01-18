
import numpy as np 
Pi = np.pi

def deg2rad(deg):
    return deg * Pi/180 

def rad2deg(rad):
    return rad * 180 / Pi

a = np.sin( deg2rad(30) )
theta = rad2deg(  np.arcsin( a )  )
