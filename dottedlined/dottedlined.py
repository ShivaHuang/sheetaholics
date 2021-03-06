#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import generator
import gui
import os
import wx

# Implementing Sheetaholics_DottedLined_Finished
class Sheetaholics_DottedLined_Finished( gui.Sheetaholics_DottedLined_Finished ):
	def __init__( self, parent ):
		gui.Sheetaholics_DottedLined_Finished.__init__( self, parent )
	
	# Handlers for Sheetaholics_DottedLined_Finished events.
	def btn_okOnButtonClick( self, event ):
		# TODO: Implement btn_okOnButtonClick
		self.Destroy()

# Implementing Sheetaholics_DottedLined
class SheetaholicsDottedLined( gui.Sheetaholics_DottedLined ):
    def __init__( self, parent ):
        gui.Sheetaholics_DottedLined.__init__( self, parent )
        self.dp_output.SetPath(os.path.abspath(os.path.dirname(__file__)))

    # Handlers for Sheetaholics_DottedLined events.
    def btn_genpdfOnButtonClick( self, event ):
        config = {}
        config['gridSize'] =        float(self.tc_gridsize.GetValue())
        config['pageWidth'] =       float(self.tc_pagewidth.GetValue())
        config['pageHeight'] =      float(self.tc_pageheight.GetValue())
        config['marginInner'] =     float(self.tc_innermargin.GetValue())
        config['marginOuter'] =     float(self.tc_outermargin.GetValue())
        config['marginTop'] =       float(self.tc_topmargin.GetValue())
        config['marginBottom'] =    float(self.tc_bottommargin.GetValue())
        config['dotDiameter'] =     float(self.tc_dotdiameter.GetValue())
        config['dotColor'] =        self.clrpk_dotcolor.GetColour()
        config['lineWidth'] =       float(self.tc_linewidth.GetValue())
        config['lineColor'] =       self.clrpk_linecolor.GetColour()
        config['pageCount'] =       float(self.sc_pagecount.GetValue())
        
        pdf_filename = "dottedlinedsheets_%s.pdf" % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        pdf_filename = os.path.join(self.dp_output.GetPath(), pdf_filename)
        generator.genpdf(pdf_filename, config)
        
        self.dialog = Sheetaholics_DottedLined_Finished(self)
        self.dialog.tc_pdfpath.SetValue(pdf_filename)
        self.dialog.Show()

class SheetaholicsMain(wx.App):
    def OnInit(self):
        self.m_frame = SheetaholicsDottedLined(None)
        self.m_frame.Show()
        return True

app = SheetaholicsMain(0)
app.MainLoop()
