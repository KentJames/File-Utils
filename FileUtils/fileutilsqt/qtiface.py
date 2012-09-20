# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtiface.ui'
#
# Created: Thu Sep 20 21:25:48 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QTIface(object):
    def setupUi(self, QTIface):
        QTIface.setObjectName(_fromUtf8("QTIface"))
        QTIface.resize(520, 131)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QTIface.sizePolicy().hasHeightForWidth())
        QTIface.setSizePolicy(sizePolicy)
        QTIface.setMinimumSize(QtCore.QSize(520, 131))
        QTIface.setMaximumSize(QtCore.QSize(520, 131))
        QTIface.setMouseTracking(False)
        self.centralWidget = QtGui.QWidget(QTIface)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.FileSearch = QtGui.QPushButton(self.centralWidget)
        self.FileSearch.setGeometry(QtCore.QRect(10, 10, 141, 51))
        self.FileSearch.setObjectName(_fromUtf8("FileSearch"))
        self.checksumactivate = QtGui.QPushButton(self.centralWidget)
        self.checksumactivate.setGeometry(QtCore.QRect(10, 70, 141, 51))
        self.checksumactivate.setObjectName(_fromUtf8("checksumactivate"))
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 10, 351, 111))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        QTIface.setCentralWidget(self.centralWidget)
        self.actionQuit = QtGui.QAction(QTIface)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuit_2 = QtGui.QAction(QTIface)
        self.actionQuit_2.setObjectName(_fromUtf8("actionQuit_2"))

        self.retranslateUi(QTIface)
        QtCore.QMetaObject.connectSlotsByName(QTIface)

    def retranslateUi(self, QTIface):
        QTIface.setWindowTitle(QtGui.QApplication.translate("File Utils", "File Utils", None, QtGui.QApplication.UnicodeUTF8))
        self.FileSearch.setText(QtGui.QApplication.translate("QTIface", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.checksumactivate.setText(QtGui.QApplication.translate("QTIface", "Checksum", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("QTIface", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit_2.setText(QtGui.QApplication.translate("QTIface", "Quit", None, QtGui.QApplication.UnicodeUTF8))

