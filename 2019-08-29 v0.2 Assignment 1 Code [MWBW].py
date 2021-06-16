# ADD YOUR NAME AND STUDENT NUMBER HERE

'''
Necessary modules imported
'''

import numpy as np #Standard module which provides us with arrays, math functions, and more
from matplotlib import pyplot as plt #Our plotting module
import scipy.integrate #Allows us to perform numerical integration 
from scipy.optimize import curve_fit
'''
Question 1.)a)
Define your variables and parameters
'''
L=10 #Length of box
pos=np.arange(0,L+0.1,0.1) #Vector of positions

'''
Question 1.)b.)
Function definition
'''
def psisq(pos,n,L): #Remember, arguments are separated by commas
    '''The 1D PIB PDF.  It should take as input the position 
    vector and energy level you wish to compute.
    It should return the PROBABILITY of finding the particle at each point.
    '''
    return (2/L)*(np.sin(n*np.pi*pos/L))**2 #This should be the 1D PIB PDF.  Careful with syntax here!

'''
Question 1.)c.)
'''
probability=psisq(pos,1,L) #Assign a variable, probability, to be the 1D PIB PDF for n=1

'''
Question 1.)d.) and e.)
'''

plt.plot(pos,probability) #Plot command, fill in the x- and y-variables
plt.xlabel("Position") #Fill in the title and font size for x-axis
plt.ylabel("Probability density") #Fill in the title and font size for y-axis
plt.show()

'''
Question 1.)e.)
'''

probability=psisq(pos,13,L)

plt.plot(pos,probability) #Plot command, fill in the x- and y-variables
plt.xlabel("Position") #Fill in the title and font size for x-axis
plt.ylabel("Probability density") #Fill in the title and font size for y-axis
plt.show()

'''
Question 2.)a.)
'''
result = scipy.integrate.quad(psisq,0.,10.,args=(1,L)) #The numerical integration step to check if our w.f. is normalized
result #Output the value of the integral and the error, make sure the value is what you expect!

'''
Question 2.)b.)
'''
result2=scipy.integrate.quad(psisq,L/3.,2*L/3,args=(1,L)) #Integrate between the bounds in the assignment this time
result2 #Again output the value of the integral, and the error

'''
Question 2.)c.)
'''
result3=scipy.integrate.quad(psisq,L/3.,2*L/3,args=(28,L)) #Integrate between the bounds in the assignment this time
result3 #Again output the value of the integral, and the error

'''
Question 2.)d.)
'''
# FILL IN YOUR ONE-SENTENCE RESPONSE HERE

'''
Question 2.)e.)
'''
def integrand(x,n,L):
    '''The expectation value for the position of 1D PIB with energy level n
    '''
    return x*psisq(x,n,L)


'''
Question 2.)f.)
'''
avpos=scipy.integrate.quad(integrand,0.,10.,args=(44,10))
avpos #Output the value of the average position
