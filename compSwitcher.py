#!/usr/bin/python2.7
#2013 december <december0123@gmail.com>
#Icons: mka <krzy49@gmail.com>
#Beerware licensed
#This little program is to help people experiencing video tearing
#with nVidia proprietary driver.
#All it does is it runs one of the three bash scripts
#provided with the program to switch between 
#compositors (xfwm4, dcompmgr, cairo-compgr).


import gtk
import subprocess
import os

workDir = os.path.dirname(__file__)
cSIcon = os.path.join(workDir, 'Icons/cS.png')
X4Icon = os.path.join(workDir, 'Icons/X4.png')
DMIcon = os.path.join(workDir, 'Icons/DM.png')
CCIcon = os.path.join(workDir, 'Icons/CC.png')
X4sh = os.path.join(workDir, 'Scripts/xfwm4.sh')
DMsh = os.path.join(workDir, 'Scripts/dcompmgr.sh')
CCsh = os.path.join(workDir, 'Scripts/cairo.sh')
allOffsh = os.path.join(workDir, 'Scripts/allOff.sh')

class compSwitcher:
    def __init__(self):
        self.trayIcon = gtk.StatusIcon()
        self.trayIcon.set_from_file(cSIcon)
        self.trayIcon.connect("popup-menu", self.click)
        
        xfwm4 = gtk.MenuItem("xfwm4")
        xfwm4.connect("activate", self.xfwm4)
        
        dcomp = gtk.MenuItem("dcompmgr")
        dcomp.connect("activate", self.dcomp)
        
        cairo = gtk.MenuItem("cairo-compmgr")
        cairo.connect("activate", self.cairo)
        
        allOff = gtk.MenuItem("Turn all off")
        allOff.connect("activate", self.allOff)
        
        close = gtk.MenuItem("Quit")
        close.connect("activate", gtk.main_quit)
            
        self.menu = gtk.Menu()
        self.menu.append(xfwm4)
        self.menu.append(dcomp)
        self.menu.append(cairo)
        self.menu.append(gtk.SeparatorMenuItem())
        self.menu.append(allOff)
        self.menu.append(gtk.SeparatorMenuItem())
        self.menu.append(close)
        self.menu.show_all()

    def click(self, icon, button, time):
        self.menu.popup(None, None, gtk.status_icon_position_menu, button, time, self.trayIcon)
    def xfwm4(self, widget):
        subprocess.call(X4sh)
        self.trayIcon.set_from_file(X4Icon)
    def dcomp(self, widget):
        subprocess.call(DMsh)
        self.trayIcon.set_from_file(DMIcon)
    def cairo(self, widget):
        subprocess.call(CCsh)
        self.trayIcon.set_from_file(CCIcon)
    def allOff(self, widget):
        subprocess.call(allOffsh)
        self.trayIcon.set_from_file(cSIcon)
        
compSwitcher()
gtk.main()
