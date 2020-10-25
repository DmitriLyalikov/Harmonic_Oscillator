import sympy as sym
import matplotlib.pyplot as plt

Force = sym.Symbol('Force')       #   Force(N)
Mass = sym.Symbol('Mass')         #   Mass of Object (Kg)
Distance = sym.Symbol('Distance') #   Initial Displacement (M)
A = sym.Symbol('A')               #   Amplitude
SPC = sym.Symbol('SPC')           #   Spring Constant
W = sym.Symbol('W')               #   Angular Frequency
T = sym.Symbol('T')               #   Period
X = sym.Symbol('X')               #   Displacement (M)
f = sym.Symbol('f')               #   Frequency (Hz)
t = sym.Symbol('t')               #   Time (S)
v = sym.Symbol('v')               #   Velocity (M/S)
a = sym.Symbol('a')               #   Acceleration (M/S^2)
potential = sym.Symbol('potential')
kinetic = sym.Symbol('kinetic')
total = sym.Symbol('total')

t_values = []                       #   x(t) values
v_values = []                       #   v(t) values
x_values = []                       #   a(t) values
a_values = []                       #   t intervals (x-axis)
pot_values = []
kin_values = []
total_values = []

Euler_Data = [t_values, v_values, x_values, a_values, pot_values, kin_values, total_values]

def Euler_Approx(Force = 5, Mass = 6, Distance = 3, interval = .1, Time= 10):
    A = Distance
    SPC = (Force/Mass)
    W = sym.sqrt(SPC/Mass)
    T = (2*sym.pi.evalf())/W
    f = 1/T
    I = sym.Symbol('I')
    t = sym.Symbol('time')
    time = Time
    step = sym.Symbol('step')
    I = interval                  #   Size of interval
    step = time/I                 #   Number of intervals
    i = I
    while i < step:
        X = (A*(sym.cos(W*i)))    #   X(t)
        v = (-W)*A*(sym.sin(W*i)) #   V(t)
        a = -(W)*X                #   a(t)
        kinetic = .5*Mass*(v**2)
        potential = .5*SPC*(X**2)
        total = kinetic + potential
        t_values.append(i)
        v_values.append(v)
        x_values.append(X)
        a_values.append(a)
        pot_values.append(potential)
        kin_values.append(kinetic)
        total_values.append(total)
        i += I
    return Euler_Data
