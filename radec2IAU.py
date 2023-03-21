# -*- coding: utf-8 -*-

"""
Function
	Converts ra, dec in degrees to extended IAU name.
	Parameters
	----------
	crval1 : float
    right ascension in decimal degrees to be converted to +hh:mm:ss.s notation
		
	crval2 : float
    declination in decimal degrees to be converted to +dd:mm:ss.s notation
		
	Returns 
	-------
extended IAU name as Jhhmmss.ss+ddmmss.s

# example 
radec2IAU(150.9887343, 3.401919528) 
              returns 'J100357.3+032406.9'

"""

import math

def radec2IAU(crval1, crval2):
    if (crval1 >= 0. and crval1 <= 360. 
        and crval2 >= -90. and crval2 <= 90.):
        crval= crval1*24/360
        (hfrac, hd1) = math.modf(crval)
        (min_frac, m1) = math.modf(hfrac * 60)
        s1 = min_frac * 60.
        (hfrac, hd2) = math.modf(crval2)
        (min_frac, m2) = math.modf(hfrac * 60)
        s2 = min_frac * 60.
        y= (int(hd1), int(m1), round(s1,1), int(hd2), int(abs(m2)), round(abs(s2),1))
	        if crval2 >= 0:
            sign = "+"
        else:
            sign = "-"
            
        y= (int(hd1), int(m1), round(s1,1), int(hd2), int(abs(m2)), round(abs(s2),1))
        IAUname = 'J'+("{0:02d}{1:02d}{2}".format(y[0], y[1],str.rjust(str(y[2]),4,'0'))) + sign + ("{0:03d}{1:02d}{2}".format( y[3], y[4],str.rjust(str(y[5]),4,'0')))
        return IAUname, y, crval1, crval2   
        IAUname='J'+("{0:02d}{1:02d}{2}{3:+03d}{4:02d}{5}".format(y[0], y[1],str.rjust(str(y[2]),4,'0'), y[3], y[4],str.rjust(str(y[5]),4,'0')))
        return IAUname, y, crval1, crval2
    else:
        error = 'wrong input values or not in range'
        return error, crval1, crval2
