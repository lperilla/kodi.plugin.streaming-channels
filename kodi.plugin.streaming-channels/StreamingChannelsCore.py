import ConfigParser
import cookielib
import os
import re
import simplejson
import subprocess
import sys
import urllib
import urllib2

import xml.dom.minidom as minidom

class StreamingChannelsCore():
    def __init__(self, instanceId=10, platformId=4, version=10):
        self.settings = sys.modules["__main__"].settings
        self.plugin = sys.modules["__main__"].plugin
        self.enabledebug = sys.modules["__main__"].enabledebug
        self.url = sys.modules["__main__"].urlChannels
        urllib2.install_opener(sys.modules["__main__"].opener)

    def getChannelLibrary(self):
        return self.getChannels('Channels', self.url)

    def getChannels(self, channelName, url):
        req = urllib2.Request(url)
        f = urllib2.urlopen(req)
        result = simplejson.load(f)
        f.close()
        
        if self.enabledebug == True:
            print result[channelName]
        return result[channelName]