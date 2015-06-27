import sys
import urlparse

class StreamingChannelsNavigation():

	def __init__(self):
		self.xbmc = sys.modules["__main__"].xbmc
		self.xbmcgui = sys.modules["__main__"].xbmcgui
		self.xbmcplugin = sys.modules["__main__"].xbmcplugin
		self.settings = sys.modules["__main__"].settings
		self.plugin = sys.modules["__main__"].plugin
		self.enabledebug = sys.modules["__main__"].enabledebug
		self.language = sys.modules["__main__"].language
		self.core = sys.modules["__main__"].core
		self.common = sys.modules["__main__"].common
		self.pluginsettings = sys.modules["__main__"].pluginsettings
		self.base_url = sys.argv[0]
		self.addon_handle = int(sys.argv[1])
		self.args = urlparse.parse_qs(sys.argv[2][1:])
		self.xbmcplugin.setContent(self.addon_handle, 'movies')
		
	def loadCategoryMenu(self):
		channelLibrary = self.core.getChannelLibrary()
		for library in channelLibrary:
			item = library.get
			id_category = item('id')
			url_category = item('url')
			url = self.core.buildUrl(self.base_url, {'mode': 'folder', 'category': id_category, 'url':url_category})
			listItem = self.xbmcgui.ListItem(id_category, iconImage = 'DefaultFolder.png')
			self.xbmcplugin.addDirectoryItem(handle = self.addon_handle, url = url, listitem = listItem, isFolder = True)

		self.xbmcplugin.endOfDirectory(self.addon_handle)
		
	def loadChannelsMenu(self):
		urlCategory = self.args['url'][0]
		nameCategory = self.args['category'][0] 
		channels = self.core.getChannels(nameCategory, urlCategory)
		for channel in channels:
			item = channel.get
			url_channel = item('url')
			img_channel = item('image')
			title_channel = item('title')
			li = self.xbmcgui.ListItem(title_channel, iconImage = img_channel, thumbnailImage = img_channel)
			self.xbmcplugin.addDirectoryItem(handle = self.addon_handle, url = url_channel, listitem = li)
			
		self.xbmcplugin.endOfDirectory(self.addon_handle)
	
	def loadMenu(self, params = {}):
		mode = self.args.get('mode', None)
		if mode is None:
			self.loadCategoryMenu()
	
		elif mode[0] == 'folder':
			self.loadChannelsMenu()

		self.common.log("Done", 5)