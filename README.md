Author: Dmitri Lyalikov
Rev. A1, 9/1/2020

Scope:
    Model Simple Harmonic Motion using differential equations in python, displaying real time values of displacement, force, acceleration and velocity. Also displaying kinetic/potential energy proportions and statisistical representation over given time frame.

Dependencies: Python 3.7 or newer. The Following Libraries are necessary to run
    pip install tkinter  -> Standard GUI library to toggle values in real time
    pip install keyboard -> Real Time keyboard interface to toggle force applied
    pip install PyQt5 -> Embedded C++ optimization for differentiation in real time
    pip install matplotlib -> Generic plotting library for static representation

To Begin Simulation:
    Run in Powershell, Command Prompt, or Terminal. Should work regardless of Host OS.
       python ./Harmonic_Oscillator.py
    keyboard input 1-4 will alter force applied from [1.5, -1.5, 3, -3]. GUI(Toggle.py) will be implemented to toggle mass and spring constant as well as    display statistical representation of data between t=0 default to t = 100 seconds or another manually given time period

Known Issues:
    When terminating, some threads may continue to run depending on sequence, until fixed, Powershell may need to be restarted

Toggle:
    Constructs User interface and passes values to Harmonic Oscillator Harmonic_Oscillator.dataSendLoop() function to introduce to plot on event of value change. Will also display statistics here.

CustomFigCanvas:
    Main plot constructor for real time representation of derived values: acceleration, velocity, position, and force.

DiffEquations(Library):
    Harmonic_Oscillator.dataSendLoop() passes values to return derived values. These are library functions from an open source repository and not my own. May remain unchanged. Will add energy functions and statistical methods.

Harmonic_Oscillator:(MAIN)
    Main Constructor and File to be run for simulation. Calls instances of Toggle and CustomFigCanvas to create plot and enters datasendloop for real time value plotting.
    -May be converted to .exe when final rev is ready for transportability.
    -Should call an init method if necessary libraries are not installed on host machine. (To Be Done)
