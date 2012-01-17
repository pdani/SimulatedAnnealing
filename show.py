#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

from annealing import Annealing

class MainWindow(wx.Frame):
    def __init__(self, parent, title, annealing):
        """Sets up main window, and sets the annealing property"""
        super(MainWindow, self).__init__(parent, title=title)
        self.annealing = annealing
        self.panel = wx.Panel(self, size=(410, 410))
        self.panel.Bind(wx.EVT_PAINT, self.on_paint) 
        self.panel.Bind(wx.EVT_IDLE, self.calculate)
        self.Fit()
    
    def calculate(self, event):
        """Periodically called method for calculating new annealing iterations"""
        
        # Draw only after 10 iterations, for faster result
        for _ in xrange(10):
            self.annealing.iterate()
        self.panel.Refresh(True)
        
    def on_paint(self, event):
        """Draws the points onto the GUI canvas"""
        dc = wx.PaintDC(self.panel)
        dc.SetPen(wx.Pen('black', 1))
        dc.SetBrush(wx.Brush('black', 1))
        for point in self.annealing.state.points:
            dc.DrawCircle(point[0], point[1], 2)

if __name__ == '__main__':
    app = wx.App()
    # New annealing instance
    annealing = Annealing()
    frame = MainWindow(None, title='Annealing', annealing=annealing)
    frame.Center()
    frame.Show()
    app.MainLoop()
    