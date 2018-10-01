# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:28:48 2017

@author: chihebdaoues
"""
import tkinter as tk       

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.config(bg="#fff")
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)                    
        self.createWidgets()

    def createWidgets(self):
        top=self.winfo_toplevel()              
        top.rowconfigure(0, weight=1)            
        top.columnconfigure(0, weight=1)         
        self.rowconfigure(0, weight=1)           
        self.columnconfigure(0, weight=1)        
        self.quit = tk.Button(self, text='Quit',width=30,fg="#fff"
        ,activebackground="#00f",activeforeground="#fff"
        ,font=('Helvetica', '16','bold'), command=self.destroy)
        self.quit.grid(row=0, column=0,padx=15,pady=15,          
            sticky=tk.N+tk.S+tk.E+tk.W)
        self.canvas = tk.Canvas(self,bg="#f00")
        self.canvas.grid()
app = Application()                       
app.master.title('Sample application')    
app.mainloop()       