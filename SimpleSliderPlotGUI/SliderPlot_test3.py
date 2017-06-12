#!/usr/bin/env python
"""

ADDING PATHS TO ALL THE LINKS THAT HELPED ME. 
https://stackoverflow.com/questions/3877774/updating-a-graphs-coordinates-in-matplotlib
https://www.tutorialspoint.com/python/tk_scale.htm
http://www.python-course.eu/tkter_sliders.php
https://stackoverflow.com/questions/14508727/how-to-get-value-out-from-the-tkter-slider-scale
http://physicalmodelingwithpython.blogspot.com/2016/04/make-your-own-gui-with-python.html
https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkter-gui/
http://www.tkdocs.com/tutorial/install.html

http://www.java2s.com/Code/Python/GUI-Tk/LayoutanchorNWWandE.htm
http://effbot.org/tkinterbook/pack.htm
https://www.tutorialspoint.com/python/tk_pack.htm
https://stackoverflow.com/questions/25745011/tkinter-slider-scale-with-discrete-steps


"""
import tkinter as tk   
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')
# from mpl_toolkits.mplot3d import  axes3d,Axes3D
from matplotlib import cm
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter


#import sys

class E(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.dest)
        self.main()

    def main(self):
        #self.fig = plt.figure()
        self.initRadius         = 1
        self.initSpeed          = 3000
        self.initInterFrameDist = 4
        self.initSpacing        = 6
        self.initReserved       = 1
        self.initZrail          = 1
        self.StartS  = 1000;
        self.EndS    = self.StartS + 25*25.6;
        
        self.fig = plt.figure() #figsize=(3.5,3.5))
        #ax = Axes3D(self.fig)
        self.Radius    = tk.IntVar()
        self.Radius.set(self.initRadius)
        self.Speed     = tk.IntVar()
        self.Speed.set(self.initSpeed)
        self.InterFrameDist     = tk.IntVar()
        self.InterFrameDist.set(self.initInterFrameDist)
        self.Spacing            = tk.IntVar()
        self.Spacing.set(self.initSpacing)
        self.Reserved           = tk.IntVar()
        self.Reserved.set(self.initReserved)
        
        #x       = np.arange(0, 10, 0.2)
        #y       = np.sin(x)
        #yvar    = [y*self.Radius.get() for y in range(len(y))]
        
        self.ax1 = self.fig.add_subplot(221)
        self.ax2 = self.fig.add_subplot(222,aspect='equal')
        #ax1.plot(x, yvar,'x')
        self.ax1.plot(1, int(self.Radius.get()) ,'x')
        #self.ax2.plot(int(self.Radius.get()),1 ,'o')
        circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
        self.ax2.add_artist(circle2)

        self.exitbtn = tk.Button(self, text='Exit', command=self.destroy)
        self.exitbtn.pack(ipadx=0,side='top',anchor = 'ne')
        
        self.btn = tk.Button(self,text='Reset All inputs',command=self.resetvalues)
        self.btn.pack(ipadx=250)
        
        self.scaleRadius = tk.Scale(self, from_=350, to=550, orient = "horizontal", variable = self.Radius, command=self.myupdateScale, label = "Radius")
        self.scaleRadius.pack(ipadx=500,anchor = 'ne')
        
        self.scaleSpeed = tk.Scale(self, from_=4000, to=6000, orient = "horizontal", variable = self.Speed, command=self.myupdateScale, label = "Speed", resolution = 1000)
        self.scaleSpeed.pack(ipadx=500,anchor = 'ne')
        
        self.scaleInterFrameDist = tk.Scale(self, from_=6, to=20, orient = "horizontal", variable = self.InterFrameDist, command=self.myupdateScale, label = "InterFrameDist")
        self.scaleInterFrameDist.pack(ipadx=500,anchor = 'ne')
        
        self.scaleSpacing = tk.Scale(self, from_=4, to=10, orient = "horizontal", variable = self.Spacing, command=self.myupdateScale, label = "Spacing")
        self.scaleSpacing.pack(ipadx=500,anchor = 'ne')
        
        self.label1text = tk.StringVar()
        self.Label1 = tk.Label(self, textvariable = self.label1text) 
        self.Label1.pack(ipadx=10, anchor = 'nw')

        self.frame = tk.Frame(self)
        self.frame.pack(ipadx=500,ipady=100,fill='both', expand=1)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)

        self.canvas.get_tk_widget().pack(side='top', fill='both')
        self.canvas._tkcanvas.pack(side='top', fill='both', expand=1)
        self.canvas.draw()
        
        self.toolbar = NavigationToolbar2TkAgg( self.canvas, self )
        self.toolbar.update()
        self.toolbar.pack()
        
       

#    def valuecheck(self,value):
#        #print("Incomplete function")
#        self.Speedlist  = [3000, 5000, 6000]
#        self.newvalue   = min(self.Speedlist, key=lambda x:abs(x-float(self.Speed.get())))
#        self.Speed.set(self.newvalue)
#        print("NewValue = " + str(self.Speed.get()))
#        self.myupdateScale(1)
        #slider.set(newvalue)
    
    def resetvalues(self):
        print('Reset function called')
        self.Radius.set(self.initRadius)
        self.Speed.set(self.initSpeed)
        self.InterFrameDist.set(self.initInterFrameDist)
        self.Spacing.set(self.initSpacing)
        self.Reserved.set(self.initReserved)
        self.myupdateScale(1) # SEND A RANDOM NUMBER 
        
    def dest(self):
        self.destroy()
        sys.exit()
    def myupdateScale(self,insidefunvar):
        print('updating scale value')
        self.ax1.clear()
        self.ax2.clear()
        self.ax1.plot(1, int(self.Radius.get()) ,'x')
        circle2 = plt.Circle((0.5, 0.5), self.Radius.get()/1000, color='blue',)
        print(self.Radius.get()/100)
        self.ax2.add_artist(circle2)
        
        self.Speedlist  = [3000, 5000, 6000]
        self.SpeedInternal   = min(self.Speedlist, key=lambda x:abs(x-float(self.Speed.get())))
        
        self.label1text.set("R = " + str(self.Radius.get()) + ",Speed =" + str(self.SpeedInternal) +
                            ",Spacing =" + str(self.Spacing.get()) + ",IFD =" + str(self.InterFrameDist.get())
                            )
        self.canvas.show()
            
if __name__ == "__main__":
    app = E(None)
    app.title('Sample GUI')
    app.mainloop()
    