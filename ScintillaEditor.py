import wx, wx.stc

from dejan7.wx.stc.mixins.DisableDragStartMixin import *
from dejan7.wx.stc.mixins.DrawColumnEndMixin import *
from dejan7.wx.stc.mixins.DrawLineBorderMixin import *
from dejan7.wx.stc.mixins.LineNumberMarginAutoWidthMixin import *

from Config import *

class ScintillaEditor(wx.stc.StyledTextCtrl):

	def __init__(self, parent):
		wx.stc.StyledTextCtrl.__init__(self, parent)
		DisableDragStartMixin(self)
		LineNumberMarginAutoWidthMixin(self)
		DrawLineBorderMixin(self, color="BLACK", delay=0)
		DrawColumnEndMixin(self, color="WHITE", margins=[0, 1])

		# self.update_timer = wx.Timer(self)
		# self.update_timer.Start(100)

	def DoTest(self):
		print "ScintillaEditor.DoTest"

		wf = self.GetWrapVisualFlags()
		wf_off = wf == wx.stc.STC_WRAPVISUALFLAG_NONE
		if wf_off: self.SetWrapVisualFlags(wx.stc.STC_WRAPVISUALFLAG_END)
		else: self.SetWrapVisualFlags(wx.stc.STC_WRAPVISUALFLAG_NONE)

def LoadStyleFromIni(scintillaEditor):
	cfg = Config()

	scintillaEditor.SetWrapMode(wx.stc.STC_WRAP_WORD)
	scintillaEditor.SetWrapVisualFlags(wx.stc.STC_WRAPVISUALFLAG_END)

	scintillaEditor.SetLexer(cfg.getint("editor", "syntax", 3))
	# PrintLexerProperties(scintillaEditor)

	scintillaEditor.SetTabWidth(cfg.getint("editor", "tabWidth", 4))

	scintillaEditor.StyleSetFont(wx.stc.STC_STYLE_DEFAULT, wx.FFont(cfg.getint("editor", "default.font.size", 16), wx.MODERN, face=cfg.get("editor", "default.font.face", ""), flags=wx.FONTFLAG_ANTIALIASED))

	scintillaEditor.SetKeyWords(0, cfg.get("editor", "keywords1", ""))
	scintillaEditor.SetKeyWords(1, cfg.get("editor", "keywords2", ""))

	defaultFg = cfg.get("editor", "default.fg", "#000000")
	defaultBg = cfg.get("editor", "default.bg", "#ffffff")

	def set_fb(id, prefix):
		scintillaEditor.StyleSetForeground(id,
			cfg.get("editor", prefix + ".fg", defaultFg))
		scintillaEditor.StyleSetBackground(id,
			cfg.get("editor", prefix + ".bg", defaultBg))

	set_fb(wx.stc.STC_STYLE_DEFAULT, "default")
	set_fb(wx.stc.STC_C_DEFAULT, "default")

	set_fb(wx.stc.STC_C_COMMENT, "comment")
	set_fb(wx.stc.STC_C_COMMENTLINE, "comment")
	set_fb(wx.stc.STC_C_IDENTIFIER, "identifier")
	set_fb(wx.stc.STC_C_NUMBER, "number")
	set_fb(wx.stc.STC_C_OPERATOR, "operator")
	set_fb(wx.stc.STC_C_PREPROCESSOR, "preprocessor")
	set_fb(wx.stc.STC_C_STRING, "string")
	set_fb(wx.stc.STC_C_WORD, "keyword1")
	set_fb(wx.stc.STC_C_WORD2, "keyword2")
	set_fb(wx.stc.STC_STYLE_LINENUMBER, "lineNr")

	scintillaEditor.SetCaretPeriod(0)
	scintillaEditor.SetCaretForeground("#f9ae58")
	scintillaEditor.SetCaretWidth(3)

	scintillaEditor.StyleSetFont(wx.stc.STC_STYLE_LINENUMBER, wx.FFont(12, wx.MODERN, flags=wx.FONTFLAG_ANTIALIASED))

	scintillaEditor.SetMarginWidth(0, scintillaEditor.TextWidth(wx.stc.STC_STYLE_LINENUMBER, "_9"))
	scintillaEditor.SetMarginWidth(1, 16)

	scintillaEditor.SetWrapMode(wx.stc.STC_WRAP_CHAR)
	scintillaEditor.SetWrapVisualFlags(wx.stc.STC_WRAPVISUALFLAG_NONE)
	scintillaEditor.SetWrapVisualFlagsLocation(wx.stc.STC_WRAPVISUALFLAGLOC_DEFAULT)
	scintillaEditor.SetWrapStartIndent(0)

	# scintillaEditor.SetBufferedDraw(1)
	# scintillaEditor.SetTwoPhaseDraw(1)
	# scintillaEditor.SetPhasesDraw(wx.stc.STC_PHASES_MULTIPLE)

	scintillaEditor.SetLayoutCache(wx.stc.STC_CACHE_DOCUMENT)
	# scintillaEditor.SetMarginOptions(wx.stc.STC_MARGINOPTION_SUBLINESELECT)
