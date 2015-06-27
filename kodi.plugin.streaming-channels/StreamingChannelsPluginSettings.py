import sys

class StreamingChannelsPluginSettings():

    def __init__(self):
        self.settings = sys.modules["__main__"].settings
        self.enabledebug = sys.modules["__main__"].enabledebug

    def isEnableDebug(self):
        return self.settings.getSetting("enabledebug") == "true"