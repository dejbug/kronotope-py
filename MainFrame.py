import wx
# from wx.lib.pubsub import pub

from dejan7.wx.Accels import *
from dejan7.wx.mixins.NoEraseBackgroundMixin import *

from ScintillaEditor import *

class MainFrame(wx.Frame):

	def __init__(self, title):
		wx.Frame.__init__(self, parent=None, title=title, size=(640,480))
		NoEraseBackgroundMixin(self)

		acc = Accels()
		acc.Add(key=wx.WXK_ESCAPE, cb=self.OnAccelEscape)
		acc.Add(key=wx.WXK_F8, cb=self.OnAccelF8)
		acc.Install(self)

		self.edit = ScintillaEditor(self)
		LoadStyleFromIni(self.edit)

		self.edit.SetText("#include <stdio.h>\n\nint main(int argc, char ** /*argv*/)\n{\n\treturn argc;\n}\n")

		self.Centre()
		self.Show()

	def OnAccelF8(self, key, mod):
		# print "* F8 pressed"
		self.edit.DoTest()

	def OnAccelEscape(self, key, mod):
		self.Close()
