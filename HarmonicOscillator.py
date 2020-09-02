#Author: Dmitri Lyalikov
#Rev. A0, 8/28/2020
#try:
import sys

import numpy as np
import random as rd

from DiffEquations import *
from CustomFigCanvas import CustomFigCanvas

import PyQt5.QtCore as QtCore
import PyQt5.QtGui  as QtGui
from PyQt5.QtWidgets import *

from Toggle import Toggle

    # for egram
import threading
import keyboard
import time

#except:
#    from Init import init_modules #If Libraries are not installed
#    init_modules()

def setCustomSize(x, width, height):
    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(x.sizePolicy().hasHeightForWidth())
    x.setSizePolicy(sizePolicy)
    x.setMinimumSize(QtCore.QSize(width, height))
    x.setMaximumSize(QtCore.QSize(width, height))

class CustomMainWindow(QMainWindow):

    def __init__(self):

        super(CustomMainWindow, self).__init__()

        # Define the geometry of the main window
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("Harmonic Oscillator")

        # Create FRAME_A
        self.Frame = QFrame(self)
        self.Frame.setStyleSheet("QWidget { background-color: %s }" % QtGui.QColor(210,210,235,255).name())
        self.layout = QGridLayout()
        self.Frame.setLayout(self.layout)
        self.setCentralWidget(self.Frame)

        # Place the matplotlib figure
        self.figure = CustomFigCanvas()
        self.layout.addWidget(self.figure, *(0,1))

        # Add the callback to ..
        myDataLoop = threading.Thread(target = dataSendLoop, daemon = True, args = (self.data_callback,))
        myDataLoop.start()

        self.show()

    def data_callback(self, v1,v2,v3,v4):
        self.figure.add_data(v1,v2,v3,v4)

class Communicate(QtCore.QObject):
    data_signal = QtCore.pyqtSignal((float,float,float,float))

def dataSendLoop(data_callback):
    # Setup the signal-slot mechanism.
    source = Communicate()
    source.data_signal.connect(data_callback)

    i = 0
#Default Values
    springconst = 5 #Newtons
    force = 0 #Newtons
    pos = 0 #Meters
    vel = 0 #Meters per Second
    mass = 5 #Grams
    dampening = 0
    w = 1 #2πf
#Corollary Values
    target = 0
    prev_target = 0
    while(True):
        prev_target = target

        # set target
        if keyboard.is_pressed('1'):
            target = 1.5
        elif keyboard.is_pressed('2'):
            target = -1.5
        elif keyboard.is_pressed('3'):
            target = 3
        elif keyboard.is_pressed('4'):
            target = -3
        elif keyboard.is_pressed('5'):
            mass = 10
        elif keyboard.is_pressed('6'):
            mass = .5
        elif keyboard.is_pressed('7'):
            w =2
        else:
            target = 0

        if target != prev_target:
            i = 0
        # move force towards target
        if abs(force-target) > 0.01:

            if force>target:
                force = force - abs(force-target)/4
            else:
                force = force + abs(force-target)/4

        else:
            force = target

        # calculate equations for main values
        y = get_f(mass,dampening,w,force,pos,vel)
        dy = get_df(mass,dampening,w,force,pos,vel)
        ddy = get_ddf(mass,dampening,w,force,pos,vel)

        time.sleep(0.01) #time delay of plot refresh
        coeff = 200 # sampling rate

        #individual points on graph at 200
        pos = y(i/coeff).real #get real portion of object returned by DiffEquations()
        vel = dy(i/coeff).real
        acc = ddy(i/coeff).real

        source.data_signal.emit(pos,vel,acc,target)
        i += 1


if __name__== '__main__':
    app = QApplication(sys.argv)
    Toggle = Toggle()
    QApplication.setStyle(QStyleFactory.create('Plastique'))
    myGUI = CustomMainWindow()
    Toggle.mainloop()

    sys.exit(app.exec_())
