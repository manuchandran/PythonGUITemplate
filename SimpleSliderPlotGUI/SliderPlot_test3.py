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
        self.fig = plt.figure(figsize=(3.5,3.5))
        #ax = Axes3D(self.fig)
        self.var     = tk.IntVar()
        x       = np.arange(0, 10, 0.2)
        y       = np.sin(x)
        yvar    = [y*self.var.get() for y in range(len(y))]
        
        self.ax1 = self.fig.add_subplot(111)
        #ax1.plot(x, yvar,'x')
        self.ax1.plot(1, int(self.var.get()) ,'x')
    
#     prop = 10
#        u = np.linspace(0, 2 * np.pi, 100)
#        v = np.linspace(0, np.pi, 100)
#        x = prop * np.outer(np.cos(u), np.sin(v))
#        y = prop * np.outer(np.sin(u), np.sin(v))
#        z = prop * np.outer(np.ones(np.size(u)), np.cos(v))

       # t = ax.plot_surface(x, y, z,  rstride=4, cstride=4,color='lightgreen',linewidth=0)


        self.frame = tk.Frame(self)
        self.frame.pack(padx=15,pady=15)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)

        self.canvas.get_tk_widget().pack(side='top', fill='both')
        self.canvas._tkcanvas.pack(side='top', fill='both', expand=1)
        self.canvas.draw()

        #self.toolbar = NavigationToolbar2TkAgg( self.canvas, self )
        #self.toolbar.update()
        #self.toolbar.pack()

        self.Label1 = tk.Label(self,textvariable = self.var) 
        self.Label1.pack(ipadx=10)
        
        self.btn = tk.Button(self,text='button',command=self.alt)
        self.btn.pack(ipadx=250)
        
        #master = tk.Tk()
      
        #Label(root, textvariable=var).pack()
        #Scale(root, from_=-2.0, to=10.0, variable=var).pack()

        self.scale1 = tk.Scale(self, from_=1, to=10, orient = "horizontal", variable = self.var, command=self.myupdateScale)
        self.scale1.pack(ipadx=0)
        self.exitbtn = tk.Button(self, text='Exit', command=self.destroy)
        self.exitbtn.pack(ipadx=500)
        #print(var)

    def alt(self):
         print('alt function called')
    def dest(self):
        self.destroy()
        sys.exit()
    def myupdateScale(self,insidefunvar):
        print('updating scale value')
        self.ax1.plot(1, int(self.var.get()) ,'x')
        self.canvas.show()
        

if __name__ == "__main__":
    app = E(None)
    app.title('Embedding in TK')
    app.mainloop()