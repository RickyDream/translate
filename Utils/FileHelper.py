# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/3/18 10:21
# __fileName__ : GoldenCoordinateV2 FileHelper.py
# __devIDE__ : PyCharm
from PySide2 import QtCore as qtc
import copy


def getDir(fileDirPath, customDir=None):
    fileDir = customDir if customDir else qtc.QDir.home()
    flag = fileDir.cd(fileDirPath)
    if not flag:
        fileDir.mkpath(fileDirPath)
        fileDir.cd(fileDirPath)
    return fileDir
def copyFile(fileName:str, fileDirPath, customDir=None):
    fileDir = getDir(fileDirPath, customDir=customDir)
    newName = fileDir.filePath(fileName.split('/')[-1])
    qtc.QFile.copy(fileName, newName)
    return newName



def mkdir(fileDirPath, customDir=None,clearFlag=True):
    fileDir = customDir if customDir else qtc.QDir.home()
    fileDir_ = copy.deepcopy(fileDir)
    flag = fileDir.cd(fileDirPath)
    if flag:
        if clearFlag:
            f = fileDir.removeRecursively()
            print(f"删除目录: {fileDirPath}", f)
    # fileDir = customDir if customDir else qtc.QDir.home()
    # while not fileDir.mkpath(fileDirPath):
    #     qtc.QThread.msleep(200)
    #     print("创建目录: $home/.jzb/bak")
    else:
        while not fileDir_.mkpath(fileDirPath):
            qtc.QThread.msleep(200)
            print(f"创建目录: {fileDirPath}")

def deleteBak(dirPath):
    fileDir = qtc.QDir(dirPath)
    entryInfoList = fileDir.entryInfoList(filters=qtc.QDir.Filter.Files)
    for entryInfo in entryInfoList:
        entryInfo: qtc.QFileInfo

        if entryInfo.suffix() == 'bak':
            fileName = entryInfo.fileName()
            b = fileDir.remove(fileName)
            # print(b)






if __name__ == '__main__':
    deleteBak('D:\Python_Study\PythonGuiPrograming\PyQt系列\project\GoldenCoordinateV2\Tests')