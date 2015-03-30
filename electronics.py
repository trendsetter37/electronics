import math

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
    # convert capacitance and inductance from strings
    # to there respective base values
    units = {
        'T'   : 1000000000000,
        'G'   : 1000000000,
        'M'   : 1000000,
        'k'   : 1000,
        'h'   : 100,
        'da'  : 10,
        'base': 1,
        'd'   : .1,
        'c'   : .01,
        'm'   : .001,
        'u'   : .000001,
        'n'   : .000000001,
        'p'   : 0.000000000001
    }

    units1 = {
        'tera'   : 1000000000000,
        'giga'   : 1000000000,
        'mega'   : 1000000,
        'kilo'   : 1000,
        'hecta'   : 100,
        'deca'  : 10,
        'base': 1,
        'deci'   : .1,
        'centi'   : .01,
        'milli'   : .001,
        'micro'   : .000001,
        'nano'   : .000000001,
        'pico'   : 0.000000000001
    }

    # This should return frequency in Hz 
    if c_unit == 'base' and i_unit == 'base':
        return 1/((2*math.pi) * math.sqrt(float(capacitance) * float(inductance)))  

    elif c_unit in units and i_unit in units:
        return  1/((2*math.pi) * math.sqrt((float(capacitance)* units[c_unit])\
                * (float(inductance)*units[i_unit])))

    elif c_unit in units1 and i_unit in units1:
        return 1/((2*math.pi) * math.sqrt((float(capacitance)* units1[c_unit])\
                * (float(inductance)*units1[i_unit])))

    
    