# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/7 15:17
# __fileName__ : GoldenCoordinateV2 Settings.py
# __devIDE__ : PyCharm


from PySide2 import QtCore as qtc
from Utils.Contants import ConfigFile,apiConfig

class Settings():


    def __init__(self, configFile):
        _Settings = qtc.QSettings(configFile, qtc.QSettings.IniFormat)
        _Settings.setIniCodec(qtc.QTextCodec.codecForName('utf-8'))
        _Settings.setAtomicSyncRequired(True)
        self._Settings = _Settings
        self._currentSec = ''

    def Keys(self, section=""):
        self._Settings.beginGroup(section)
        keys = self._Settings.childKeys()
        self._Settings.endGroup()
        return keys

    def Sections(self):
        return self._Settings.childGroups()

    def setSection(self, section):
        self._currentSec = section


    def value(self,key, defaultValue=None, type=str):
        self._Settings.beginGroup(self._currentSec)
        value = self._Settings.value(key, defaultValue=defaultValue, type=type)
        self._Settings.endGroup()
        return value

    def setValue(self,key, value):
        self._Settings.beginGroup(self._currentSec)
        self._Settings.setValue(key, value)
        self._Settings.endGroup()


globalSettings = Settings(ConfigFile)
apiSettings = Settings(apiConfig)







