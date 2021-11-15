
# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/14 17:54
# __fileName__ : GoldenCoordinateV2 折叠控件.py
# __devIDE__ : PyCharm

import sys

from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
import pyperclip



from UiFiles.Ui_TranslateAssistant import Ui_FormTranslateAssistant

from Components.BaseWidget import BaseWidget

from Translate.translate2 import google2
from Translate.codeFilter import isJavaCode
from Translate.utils import DBC2SBC






class TranslateAssistant(BaseWidget, Ui_FormTranslateAssistant):
    headerKeys = ['User-Agent', 'Host', 'Referer','Cookie','Content-Type']

    def __init__(self, *args, **kwargs):
        """MainWindow constructor"""
        super().__init__(*args, **kwargs)
        # Main UI code goes here
        # End main UI code

        self.setupUi(self)

        self.clipboard = qtw.QApplication.clipboard()



        self.initSlots()

        self.clipText = ""
        self.incrementalText = []

        self.clipOriginText = ""





    def closeEvent(self, event:qtg.QCloseEvent) -> None:
        if hasattr(self, 'hashManagerThread') and self.hashManagerThread.isRunning():
            self.hashManagerThread.quit()



    def initSlots(self):


        # 绑定剪切板数据变化事件
        # self.clipboard.dataChanged.connect(self.clipboardDataChanged)

        self.btnTranslate.clicked.connect(self.btnTranslateClicked)

        self.btnClearData.clicked.connect(self.resetTranslateState)

        self.cBMonitorClip.stateChanged.connect(self.monitorClipStateChanged)



    def monitorClipStateChanged(self, state):
        if state:
            self.clipboard.dataChanged.connect(self.clipboardDataChanged)
        else:
            self.clipboard.dataChanged.disconnect(self.clipboardDataChanged)

    def btnTranslateClicked(self):
        txt1 = ' '.join(self.incrementalText)
        txt2 = self.textEditOrigin.toPlainText()
        txt = txt1 or txt2
        if txt:
            self.translateText(txt)



    def clipboardDataChanged(self):

        mimeData = self.clipboard.mimeData()
        txt = mimeData.text()
        if mimeData.hasText() and not txt.startswith('file:///'):
            if self.clipOriginText and len(txt.split(self.clipOriginText)) == 2:
                return
            if txt and not isJavaCode(txt) and txt != self.clipText:
                print(f"当前剪切板数据为:{txt}")
                self.clipOriginText = txt
                if self.cBIncrementalCopy.isChecked():
                    self.clipText = txt
                    self.incrementalText.extend(list([v.strip() for v in txt.split() if v.strip()]))
                    self.textEditOrigin.setText(' '.join(self.incrementalText))
                else:
                    self.translateText(txt)


    def translateText(self,s):
        self.tabWidget.setCurrentWidget(self.translate)
        t = google2(s)
        res = f"{t.origin[:10]}->{t.text[:10]}"
        print(res)
        res = DBC2SBC(t.text)
        self.clipText = res
        pyperclip.copy(res)
        self.resetTranslateState(t)

    def resetTranslateState(self, t=None):
        self.textEditOrigin.setText((t and t.origin) or "")
        self.textEditDest.setText((t and t.text) or "")
        self.incrementalText.clear()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = TranslateAssistant()
    mw.show()
    sys.exit(app.exec_())


