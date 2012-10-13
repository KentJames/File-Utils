# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtiface.ui'
#
# Created: Sun Sep 23 16:11:18 2012
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
        QTIface.resize(631, 273)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QTIface.sizePolicy().hasHeightForWidth())
        QTIface.setSizePolicy(sizePolicy)
        QTIface.setMinimumSize(QtCore.QSize(631, 273))
        QTIface.setMaximumSize(QtCore.QSize(631, 273))
        QTIface.setMouseTracking(False)
        self.centralWidget = QtGui.QWidget(QTIface)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.FileSearch = QtGui.QPushButton(self.centralWidget)
        self.FileSearch.setGeometry(QtCore.QRect(10, 10, 141, 51))
        self.FileSearch.setObjectName(_fromUtf8("FileSearch"))
        self.checksumactivate = QtGui.QPushButton(self.centralWidget)
        self.checksumactivate.setGeometry(QtCore.QRect(440, 210, 181, 31))
        self.checksumactivate.setObjectName(_fromUtf8("checksumactivate"))
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 10, 461, 191))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.checksumtypeselection = QtGui.QComboBox(self.centralWidget)
        self.checksumtypeselection.setGeometry(QtCore.QRect(270, 210, 161, 31))
        self.checksumtypeselection.setObjectName(_fromUtf8("checksumtypeselection"))
        self.checksumtypeselection.addItem(_fromUtf8(""))
        self.checksumtypeselection.addItem(_fromUtf8(""))
        self.checksumtypeselection.addItem(_fromUtf8(""))
        self.checksumtypeselection.addItem(_fromUtf8(""))
        self.checksumtypeselection.addItem(_fromUtf8(""))
        self.checksumtypeselection.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(170, 210, 91, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.cleartextboxbutton = QtGui.QPushButton(self.centralWidget)
        self.cleartextboxbutton.setGeometry(QtCore.QRect(10, 70, 141, 51))
        self.cleartextboxbutton.setObjectName(_fromUtf8("cleartextboxbutton"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 131, 121))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        QTIface.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(QTIface)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 631, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        QTIface.setMenuBar(self.menuBar)
        self.actionSave_hash_as = QtGui.QAction(QTIface)
        self.actionSave_hash_as.setObjectName(_fromUtf8("actionSave_hash_as"))
        self.actionQuit_3 = QtGui.QAction(QTIface)
        self.actionQuit_3.setObjectName(_fromUtf8("actionQuit_3"))
        self.actionHelp = QtGui.QAction(QTIface)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(QTIface)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionSave_hash_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_3)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(QTIface)
        QtCore.QMetaObject.connectSlotsByName(QTIface)

    def retranslateUi(self, QTIface):
        QTIface.setWindowTitle(QtGui.QApplication.translate("QTIface", "QTIface", None, QtGui.QApplication.UnicodeUTF8))
        self.FileSearch.setText(QtGui.QApplication.translate("QTIface", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.checksumactivate.setText(QtGui.QApplication.translate("QTIface", "Generate Hash", None, QtGui.QApplication.UnicodeUTF8))
        self.checksumtypeselection.setItemText(0, QtGui.QApplication.translate("QTIface", "md5", None, QtGui.QApplication.UnicodeUTF8))
        self.checksumtypeselection.setItemText(1, QtGui.QApplication.translate("QTIface", "sha1", None, QtGui.QApplication.UnicodeUTF8))
        self.checksumtypeselection.setItemText(2, QtGui.QApplication.translate("QTIface", "sha224", None, QtGui.QApplication.UnicodeUTF8))
        self.checksumtypeselection.setItemText(3, QtGui.QApplication.translate("QTIface", "sha256", None, QtGui.QApplication.UnicodeUTF8))
        self.checksumtypeselection.setItemText(4, QtGui.QApplication.translate("QTIface", "sha384", None, QtGui.QApplication.UnicodeUTF8))
        self.checksumtypeselection.setItemText(5, QtGui.QApplication.translate("QTIface", "sha512", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("QTIface", "Hash Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cleartextboxbutton.setText(QtGui.QApplication.translate("QTIface", "Clear All", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("QTIface", "1) Browse for file\n"
"\n"
"2) Select hash type\n"
"\n"
"3) Click Generate Hash.", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("QTIface", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("QTIface", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_hash_as.setText(QtGui.QApplication.translate("QTIface", "Save hash as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit_3.setText(QtGui.QApplication.translate("QTIface", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("QTIface", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("QTIface", "About", None, QtGui.QApplication.UnicodeUTF8))

