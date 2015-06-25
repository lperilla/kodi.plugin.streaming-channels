import os
import sys
import urllib
import urllib2

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

    def listMenu(self, params={}):
        self.common.log(repr(params), 1)
        get = params.get

        channelLibrary = self.core.getChannelLibrary()

        for library in channelLibrary:
            item = library.get
            libraryId = item('id')
            libraryUrl = item('url')
            #self.addDir(libraryId, libraryUrl, sys.argv[1], "")
            channels = self.core.getChannels(libraryId, libraryUrl)
            for channel in channels:
                self.addListItem(params, channel)
        self.xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
        
        self.common.log("Done", 5)

    def addListItem(self, params={}, item_params={}):
        item = item_params.get
        url = item('url')
        image = item('image')
        title = item('title')
        
        contextmenu = [(self.language(3001), "XBMC.RunPlugin(%s?path=refresh" %(sys.argv[0],))]
        
        fanart = os.path.join(self.settings.getAddonInfo("path"), "fanart.jpg")

        listitem = self.xbmcgui.ListItem(title, iconImage=image, thumbnailImage=image)
        listitem.addContextMenuItems(items=contextmenu, replaceItems=True)
        listitem.setProperty("fanart_image", fanart)
        listitem.setProperty('IsPlayable', "true")
        listitem.setInfo('Video', {'Title': title})

        ok = self.xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=listitem, isFolder=False)

        self.common.log("Done", 5)
    
    def addDir(self, name, url, mode, image):
        urlStr = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "name=" + urllib.quote_plus(name)
        listitem = self.xbmcgui.ListItem(unicode(name), iconImage="DefaultFolder.png", thumbnailImage=image)
        listitem.setInfo(type="Video", infoLabels={ "Title": name })
        ok = self.xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=urlStr, listitem=listitem, isFolder=True)
        return ok
