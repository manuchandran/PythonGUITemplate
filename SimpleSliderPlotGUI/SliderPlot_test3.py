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
        self.fig = plt.figure() #figsize=(3.5,3.5))
        
        #ax = Axes3D(self.fig)
        self.var     = tk.IntVar()
        x       = np.arange(0, 10, 0.2)
        y       = np.sin(x)
        yvar    = [y*self.var.get() for y in range(len(y))]
        
        self.ax1 = self.fig.add_subplot(221)
        self.ax2 = self.fig.add_subplot(222)
        #ax1.plot(x, yvar,'x')
        self.ax1.plot(1, int(self.var.get()) ,'x')
        self.ax2.plot(int(self.var.get()),1 ,'o')

    
#     prop = 10
#        u = np.linspace(0, 2 * np.pi, 100)
#        v = np.linspace(0, np.pi, 100)
#        x = prop * np.outer(np.cos(u), np.sin(v))
#        y = prop * np.outer(np.sin(u), np.sin(v))
#        z = prop * np.outer(np.ones(np.size(u)), np.cos(v))

       # t = ax.plot_surface(x, y, z,  rstride=4, cstride=4,color='lightgreen',linewidth=0)

        self.exitbtn = tk.Button(self, text='Exit', command=self.destroy)
        self.exitbtn.pack(ipadx=0,side='top',anchor = 'ne')
        
        self.btn = tk.Button(self,text='Reset All inputs',command=self.alt)
        self.btn.pack(ipadx=250)
        
        self.scale1 = tk.Scale(self, from_=1, to=10, orient = "horizontal", variable = self.var, command=self.myupdateScale, label = "Label1")
        self.scale1.pack(ipadx=500,anchor = 'ne')
        
        self.frame = tk.Frame(self)
        self.frame.pack(ipadx=500,ipady=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)

        self.canvas.get_tk_widget().pack(side='top', fill='both')
        self.canvas._tkcanvas.pack(side='top', fill='both', expand=1)
        self.canvas.draw()

        self.label1text = tk.StringVar()
        self.label1text.set("My Scale value = " + str(self.var.get()) )
        self.Label1 = tk.Label(self, textvariable = self.label1text) 
        self.Label1.pack(ipadx=10, anchor = 'nw')

    def alt(self):
         print('alt function called')
    def dest(self):
        self.destroy()
        sys.exit()
    def myupdateScale(self,insidefunvar):
        print('updating scale value')
        self.ax1.clear()
        self.ax2.clear()
        self.ax1.plot(1, int(self.var.get()) ,'x')
        self.ax2.plot(int(self.var.get()),1 ,'o')
        self.label1text.set("My Scale value = " + str(self.var.get()) )
        self.canvas.show()
        

if __name__ == "__main__":
    app = E(None)
    app.title('Embedding in TK')
    app.mainloop()