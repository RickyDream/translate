# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TranslateAssistant.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FormTranslateAssistant(object):
    def setupUi(self, FormTranslateAssistant):
        if not FormTranslateAssistant.objectName():
            FormTranslateAssistant.setObjectName(u"FormTranslateAssistant")
        FormTranslateAssistant.resize(850, 640)
        FormTranslateAssistant.setMinimumSize(QSize(850, 640))
        self.verticalLayout = QVBoxLayout(FormTranslateAssistant)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.line = QFrame(FormTranslateAssistant)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.tabWidget = QTabWidget(FormTranslateAssistant)
        self.tabWidget.setObjectName(u"tabWidget")
        self.translate = QWidget()
        self.translate.setObjectName(u"translate")
        self.horizontalLayout_24 = QHBoxLayout(self.translate)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 3, 0, 0)
        self.widget_32 = QWidget(self.translate)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_26 = QVBoxLayout(self.widget_32)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        self.formLayout_3 = QFormLayout(self.widget_33)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget_33)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setLayoutDirection(Qt.RightToLeft)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.cbbSrcLang = QComboBox(self.widget_33)
        self.cbbSrcLang.addItem("")
        self.cbbSrcLang.setObjectName(u"cbbSrcLang")
        self.cbbSrcLang.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.cbbSrcLang)

        self.label_21 = QLabel(self.widget_33)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setLayoutDirection(Qt.RightToLeft)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_21)

        self.cbbDestLang = QComboBox(self.widget_33)
        self.cbbDestLang.addItem("")
        self.cbbDestLang.setObjectName(u"cbbDestLang")
        self.cbbDestLang.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.cbbDestLang)

        self.cBIncrementalCopy = QCheckBox(self.widget_33)
        self.cBIncrementalCopy.setObjectName(u"cBIncrementalCopy")

        self.formLayout_3.setWidget(2, QFormLayout.SpanningRole, self.cBIncrementalCopy)

        self.cBMonitorClip = QCheckBox(self.widget_33)
        self.cBMonitorClip.setObjectName(u"cBMonitorClip")

        self.formLayout_3.setWidget(3, QFormLayout.SpanningRole, self.cBMonitorClip)

        self.cBAutoCopy = QCheckBox(self.widget_33)
        self.cBAutoCopy.setObjectName(u"cBAutoCopy")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.cBAutoCopy)

        self.cBAutoPaste = QCheckBox(self.widget_33)
        self.cBAutoPaste.setObjectName(u"cBAutoPaste")

        self.formLayout_3.setWidget(5, QFormLayout.SpanningRole, self.cBAutoPaste)


        self.verticalLayout_26.addWidget(self.widget_33)

        self.verticalSpacer = QSpacerItem(20, 366, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer)

        self.widget_34 = QWidget(self.widget_32)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_28 = QVBoxLayout(self.widget_34)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.btnClearData = QPushButton(self.widget_34)
        self.btnClearData.setObjectName(u"btnClearData")

        self.verticalLayout_28.addWidget(self.btnClearData)

        self.btnTranslate = QPushButton(self.widget_34)
        self.btnTranslate.setObjectName(u"btnTranslate")

        self.verticalLayout_28.addWidget(self.btnTranslate)


        self.verticalLayout_26.addWidget(self.widget_34)


        self.horizontalLayout_24.addWidget(self.widget_32)

        self.widget_translate = QWidget(self.translate)
        self.widget_translate.setObjectName(u"widget_translate")
        self.verticalLayout_27 = QVBoxLayout(self.widget_translate)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget_translate)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.textEditOrigin = QTextEdit(self.splitter)
        self.textEditOrigin.setObjectName(u"textEditOrigin")
        self.splitter.addWidget(self.textEditOrigin)
        self.textEditDest = QTextEdit(self.splitter)
        self.textEditDest.setObjectName(u"textEditDest")
        self.splitter.addWidget(self.textEditDest)

        self.verticalLayout_27.addWidget(self.splitter)


        self.horizontalLayout_24.addWidget(self.widget_translate)

        self.tabWidget.addTab(self.translate, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(FormTranslateAssistant)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormTranslateAssistant)
    # setupUi

    def retranslateUi(self, FormTranslateAssistant):
        FormTranslateAssistant.setWindowTitle(QCoreApplication.translate("FormTranslateAssistant", u"Form", None))
        self.label_20.setText(QCoreApplication.translate("FormTranslateAssistant", u"\u6e90\u8bed\u8a00", None))
        self.cbbSrcLang.setItemText(0, QCoreApplication.translate("FormTranslateAssistant", u"en", None))

        self.label_21.setText(QCoreApplication.translate("FormTranslateAssistant", u"\u76ee\u6807\u8bed\u8a00", None))
        self.cbbDestLang.setItemText(0, QCoreApplication.translate("FormTranslateAssistant", u"zh-CN", None))

        self.cBIncrementalCopy.setText(QCoreApplication.translate("FormTranslateAssistant", u"\u589e\u91cf\u590d\u5236", None))
        self.cBMonitorClip.setText(QCoreApplication.translate("FormTranslateAssistant", u"\u76d1\u542c\u526a\u5207\u677f", None))
        self.cBAutoCopy.setText(QCoreApplication.translate("FormTranslateAssistant", u"\u81ea\u52a8\u590d\u5236", None))
        self.cBAutoPaste.setText(QCoreApplication.translate("FormTranslateAssistant", u"\u81ea\u52a8\u7c98\u8d34", None))
        self.btnClearData.setText(QCoreApplication.translate("FormTranslateAssistant", u"\u6570\u636e\u64e6\u9664", None))
        self.btnTranslate.setText(QCoreApplication.translate("FormTranslateAssistant", u"\u7ffb\u8bd1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.translate), QCoreApplication.translate("FormTranslateAssistant", u"\u6587\u6863\u7ffb\u8bd1", None))
    # retranslateUi

