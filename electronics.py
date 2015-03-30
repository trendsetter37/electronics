import math

def resonant_frequency(capacitance, inductance):
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
        '''
    
    return 1/((2*math.pi) * math.sqrt(float(capacitance) * inductance))