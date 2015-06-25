import cookielib
import sys
import urllib2

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin


settings = xbmcaddon.Addon(id='kodi.plugin.streaming-channels')
language = settings.getLocalizedString
enabledebug = settings.getSetting('enabledebug') == "true"
urlChannels = settings.getSetting('urlChannels')
version = settings.getSetting('version')
author = settings.getSetting('author')
plugin = 'Streaming Channels-' + version

if (enabledebug == True):
    print("--------------------------------------------")
    print("author: " + author)
    print("version: " + version)
    print("plugin: " + plugin)
    print("urlChannels: " + urlChannels)
    print("--------------------------------------------")

cookie = cookielib.LWPCookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_handler)

# Plugin Main
if (__name__ == "__main__"):
    if enabledebug:
        print("ARGV Parameters: " + repr(sys.argv))
   
    import StreamingChannelsCore
    import StreamingChannelsNavigation
    import CommonFunctions as common
    import StreamingChannelsPluginSettings
    
    common.plugin = plugin
    pluginsettings = StreamingChannelsPluginSettings.StreamingChannelsPluginSettings()
    
    core = StreamingChannelsCore.StreamingChannelsCore()
    
    navigation = StreamingChannelsNavigation.StreamingChannelsNavigation()

    navigation.listMenu()
