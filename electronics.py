import math
''' Will add command line interaction soon '''

# units to use during conversion functions
units = {
        'T'   : (1000000000000, 10**12),
        'G'   : (1000000000, 10**9),
        'M'   : (1000000, 10**6),
        'k'   : (1000, 10**3),
        'h'   : (100, 10**2),
        'da'  : (10, 10),
        'base': (1,1),
        'd'   : (0.1, 10**-1), 
        'c'   : (0.01, 10**-2),
        'm'   : (0.001, 10**-3),
        'u'   : (0.000001, 10**-6),
        'n'   : (0.000000001, 10**-9),
        'p'   : (0.000000000001, 10**-12)
    }

units1 = {
        'tera'   : (1000000000000, 10**12),
        'giga'   : (1000000000, 10**9),
        'mega'   : (1000000, 10**6),
        'kilo'   : (1000, 10**3),
        'hecta'  : (100, 10**2),
        'deca'   : (10, 10),
        'base'   : (1,1),
        'deci'   : (0.1, 10**-1),
        'centi'  : (0.01, 10**-2),
        'milli'  : (0.001, 10**-3),
        'micro'  : (0.000001, 10**-6),
        'nano'   : (0.000000001, 10**-9),
        'pico'   : (0.000000000001, 10**-12)
    }

CONSTANTS = {
    'uo'    : 4*Math.pi * 10**-7,
    'eo'    : 8.8541878*10**-12

}
# still have things to work on here
def human_readable_frequency(freq, convert_to='base', convert_from='base'):
    ''' Works a little bit. Improve functionality '''
    # TODO make printout pretty
   
    result = (freq* units1[convert_from][1]) / (units1[convert_to][1])
    return result

def resonant_frequency(capacitance, inductance, c_unit='base', i_unit='base'):
    ''' *** electronics.electronics.py
        * Useful for LC circuit work
        * Both the capacitance and inductance should be in there
          base measurment units. I.e. 100 uHz (micro-hertz) should 
          be 0.0001 Hz etc.
          
        * Resonant frequency equation is fr = 1 / (2Pi * squrt(capacitance * inductance))
        
        **********************************************************************************
        TODO make this function discriminate bewtween units so that a unit can be suffixed
        to the output, irregardless of what the inputs were (strings with unit suffixes in
        this case )
        **********************************************************************************
        Unit Table
        ----------

        |Text|Symbol|Factor|
        --------------------
        tera    T      1 000 000 000 000
        giga    G      1 000 000 000
        mega    M      1 000 000
        kilo    k      1 000
        hecto   h      1 00
        deca    da     10 # prob. will not ever use this but it's here
        (none)  (none) 1
        deci    d      0.1
        centi   c      0.01
        milli   m      0.001
        micro   µ      0.000 001 # the letter 'u' can be used here
        nano    n      0.000 000 001
        pico    p      0.000 000 000 001

        *******************************************

        **kwargs can be 'base' (automatic) or any of the prefix
        letters of above

        '''
    
    # This should return frequency in Hz 
    if c_unit == 'base' and i_unit == 'base':
        result = 1/((2*math.pi) * math.sqrt(float(capacitance) * float(inductance)))
        return result

    elif c_unit in units and i_unit in units:
        result = 1/((2*math.pi) * math.sqrt((float(capacitance)* units[c_unit])\
                * (float(inductance)*units[i_unit])))
        return result 

    elif c_unit in units1 and i_unit in units1:
        result = 1/((2*math.pi) * math.sqrt((float(capacitance)* units1[c_unit])\
                * (float(inductance)*units1[i_unit])))
        return result

    
    

def calculate_inductance(inner_radius=1, coil_length=1, coil_turns=1):
    '''
    *********************************************
    *                                           *
    * TODO: Testing, and usability prompts      *
    *********************************************
        uo is permeability of free space
        A  = inner core area pi * r^2
        l  = coil length
        uo = 4*pi*10^-7'''

    return (4*pi*10**-7) * ((coil_turns**2 * (pi * inner_radius**2))/coil_length) 

def calculate_capacitance(sphere_radius=1):
    ''' 
        Sphere radius should be in meters preferably
    '''

    return 4*pi*CONSTANTS['eo']*float(sphere_radius) # Just in case