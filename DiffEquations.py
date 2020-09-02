import cmath

'''

X = Fs/K
F = -kX
x(t) vs t - expect a cosine

v(t) vs t - expect a negative sine

K(t) = 1/2 m v^2 - expect a squared sine form

U(t) = 1/2 k x^2 - expect a squared cosine form

E(t) = K + U - expect a straight horizontal line

'''

def get_Var(Values): #Find which values are given and delegate functions to derive unkowns
    quantities = []

def get_f(A,B,C,D,E,F): #Get Position

    def f(t):
        Y = lambda A,B,C,D,E,F,t: -cmath.exp(-(B - cmath.sqrt(-4 * C * A + B ** 2)) * t / A / 2) * cmath.sqrt(-4 * C * A + B ** 2) * (2 * F * A * C + B * E * C + cmath.sqrt(-4 * C * A + B ** 2) * E * C - B * D - cmath.sqrt(-4 * C * A + B ** 2) * D) / (8 * C * A - 2 * B ** 2) / C + cmath.exp(-(B + cmath.sqrt(-4 * C * A + B ** 2)) * t / A / 2) * (2 * F * A * C + B * E * C - cmath.sqrt(-4 * C * A + B ** 2) * E * C - B * D + cmath.sqrt(-4 * C * A + B ** 2) * D) * cmath.sqrt(-4 * C * A + B ** 2) / (8 * C * A - 2 * B ** 2) / C + D / C
        return Y(A,B,C,D,E,F,t)
    return f

def get_df(A,B,C,D,E,F): #Get Velocity

    def f(t):
        dY = lambda A,B,C,D,E,F,t: (B - cmath.sqrt(-4 * C * A + B ** 2)) * cmath.exp(-(B - cmath.sqrt(-4 * C * A + B ** 2)) * t / A / 2) * cmath.sqrt(-4 * C * A + B ** 2) * (2 * F * A * C + B * E * C + cmath.sqrt(-4 * C * A + B ** 2) * E * C - B * D - cmath.sqrt(-4 * C * A + B ** 2) * D) / A / (8 * C * A - 2 * B ** 2) / C / 2 - (B + cmath.sqrt(-4 * C * A + B ** 2)) * cmath.exp(-(B + cmath.sqrt(-4 * C * A + B ** 2)) * t / A / 2) * (2 * F * A * C + B * E * C - cmath.sqrt(-4 * C * A + B ** 2) * E * C - B * D + cmath.sqrt(-4 * C * A + B ** 2) * D) * cmath.sqrt(-4 * C * A + B ** 2) / A / (8 * C * A - 2 * B ** 2) / C / 2
        return dY(A,B,C,D,E,F,t)
    return f

def get_ddf(A,B,C,D,E,F): #Get Acceleration

    def f(t):
        ddY = lambda A,B,C,D,E,F,t: -(B - cmath.sqrt(-4 * C * A + B ** 2)) ** 2 * cmath.exp(-(B - cmath.sqrt(-4 * C * A + B ** 2)) * t / A / 2) * cmath.sqrt(-4 * C * A + B ** 2) * (2 * F * A * C + B * E * C + cmath.sqrt(-4 * C * A + B ** 2) * E * C - B * D - cmath.sqrt(-4 * C * A + B ** 2) * D) / A ** 2 / (8 * C * A - 2 * B ** 2) / C / 4 + (B + cmath.sqrt(-4 * C * A + B ** 2)) ** 2 * cmath.exp(-(B + cmath.sqrt(-4 * C * A + B ** 2)) * t / A / 2) * (2 * F * A * C + B * E * C - cmath.sqrt(-4 * C * A + B ** 2) * E * C - B * D + cmath.sqrt(-4 * C * A + B ** 2) * D) * cmath.sqrt(-4 * C * A + B ** 2) / A ** 2 / (8 * C * A - 2 * B ** 2) / C / 4
        return ddY(A,B,C,D,E,F,t)
    return f
