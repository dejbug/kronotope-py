import ConfigParser

class Config(object):

	def __init__(self, path="settings.ini"):
		self.cfg = ConfigParser.RawConfigParser()
		self.cfg.read(path)

	def get(self, section, key, default=None):
		try: return self.cfg.get(section, key)
		except ConfigParser.NoSectionError: pass
		except ConfigParser.NoOptionError: pass
		return default

	def getint(self, section, key, default=None):
		try: return self.cfg.getint(section, key)
		except ConfigParser.NoSectionError: pass
		except ConfigParser.NoOptionError: pass
		return default
