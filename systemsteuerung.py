import tkinter as tk
from tkinter import ttk
import os
import time

def powercfg():
    os.popen("powercfg.cpl")
    

root = tk.Tk()

root.title("Custom System Control")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

button_powercfg = ttk.Button(text="Energieeinstellungen", command = lambda: os.popen("powercfg.cpl"))
button_ncpa= ttk.Button(text="Netzwerkverbindungen", command = lambda: os.popen("ncpa.cpl"))
button_appwiz = ttk.Button(text="Programme", command = lambda: os.popen("appwiz.cpl"))
button_sysdm = ttk.Button(text="Systemeigenschaften", command = lambda: os.popen("sysdm.cpl"))
button_firewall = ttk.Button(text="Firewall", command = lambda: os.popen("firewall.cpl"))
button_3dx = ttk.Button(text="3DX_GUI", command = lambda: os.popen("Launch3DxGUI.cpl"))
button_hdwwiz = ttk.Button(text="Geräte-Manager", command = lambda: os.popen("hdwwiz.cpl"))
button_diskmgmt = ttk.Button(text="Datenträgerverwaltung", command = lambda: os.popen("diskmgmt.msc"))
#button_hdwwiz = ttk.Button(text="", command = lambda: os.popen("hdwwiz.cpl"))

button_powercfg.pack()
button_ncpa.pack()
button_appwiz.pack()
button_sysdm.pack()
button_firewall.pack()
button_3dx.pack()
button_hdwwiz.pack()
button_diskmgmt.pack()


#os.popen("ncpa.cpl")
#os.popen("appwiz.cpl")



root.mainloop()
