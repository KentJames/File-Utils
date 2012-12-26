# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
#
# Created: Sun Oct 14 16:18:42 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(462, 187)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 171))
        self.label.setFrameShape(QtGui.QFrame.Panel)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 171, 171))
        self.label_2.setFrameShape(QtGui.QFrame.Panel)
        self.label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(260, 10, 20, 171))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

