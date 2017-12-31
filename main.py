import wx

from MainFrame import *

TITLE = "kronotope-py"
VENDOR = "dejbug.de"

def main():
	a = wx.App()
	f = MainFrame(title=TITLE)
	a.MainLoop()

if "__main__" == __name__:
	main()
