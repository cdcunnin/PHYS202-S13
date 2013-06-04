import numpy as np

def linleastsquaresfit(x,y):

    """Takes in arrays representing (x,y) values and performs a linear least squares regression. Returns slope (m), intercept (b), and uncertainty in both of the best linear fit in the following array: [m,b,uncm,uncb]"""
    
    import numpy as np

    X = (1./len(x))*sum(x)
    X2 = (1./len(x))*sum(x**2)
    Y = (1./len(y))*sum(y)
    XY = (1./len(x))*sum(x*y)
    m = ((XY)-(X*Y))/(X2-X**2)
    b = ((X2*Y-X*XY))/(X2-X**2)
    delta = y-(m*x+b)
    uncm = np.sqrt((1./(len(x)-2))*((sum(delta**2))/(-sum(x**2)+(sum(x))**2)))
    uncb = np.sqrt((1./(len(x)-2))*((sum(delta**2)*sum(x**2))/(-sum(x**2)+(sum(x))**2)))
    uncy = np.sqrt((1./(len(y)-2))*sum(delta**2))
    print "uncertainty in y = " + str(uncy)
    print "m = " + str(m)
    print "b = " + str(b)
    print "uncertainty in m: " + str(uncm)
    print "uncertainty in b: " + str(uncb)
    return [m,b,uncm,uncb]

def weightedlinleastsqaresfit(x,y,w):

    """Take in values for x and y points, and the weighting w for each. Return the slope (m), intercept (b), and the uncertainty in each in the following array: [m,b,unc,uncb]"""

    import numpy as np

    m = (sum(w)*sum(w*x*y)-sum(w*x)*sum(w*y))/(sum(w)*sum(w*x**2)-(sum(w*x))**2)
    b = (sum(w*x**2)*sum(w*y)-sum(w*x)*sum(w*x*y))/(sum(w)*sum(w*x**2)-(sum(w*x))**2)
    uncm = np.sqrt(sum(w)/(sum(w)*(sum(w*x**2)-(sum(w*x))**2)))
    uncb = np.sqrt(sum(w*x**2)/(sum(w)*(sum(w*x**2)-(sum(w*x))**2)))
    
    print "m = " + str(m)
    print "b = " + str(b)
    print "uncertainty in m " + str(uncm)
    print "uncertainty in b " + str(uncb)
    
    return [m,b,uncm,uncb]
