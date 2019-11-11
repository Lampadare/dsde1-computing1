import math

def period(L, g):

    Boal_one = isinstance(L, str)
    Boal_two = isinstance(g, str)

    if Boal_one or Boal_two == True:
        raise(TypeError)

    elif g == 0:
        raise(ValueError)

    else :
        T = ((2*math.pi)*(math.sqrt(L/g)))
        print('Period =', T)
        print('Your math has been executed :)')
        return T
print('yey')
