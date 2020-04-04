# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Programming\CodeProjects\QffmpegUI\QffmpegUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_winMain(object):
    def setupUi(self, winMain):
        winMain.setObjectName("winMain")
        winMain.resize(413, 190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(winMain.sizePolicy().hasHeightForWidth())
        winMain.setSizePolicy(sizePolicy)
        winMain.setMinimumSize(QtCore.QSize(413, 190))
        winMain.setMaximumSize(QtCore.QSize(413, 190))
        self.centralwidget = QtWidgets.QWidget(winMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 391, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tabFile = QtWidgets.QWidget()
        self.tabFile.setObjectName("tabFile")
        self.btnFileBrowser = QtWidgets.QPushButton(self.tabFile)
        self.btnFileBrowser.setGeometry(QtCore.QRect(315, 7, 61, 20))
        self.btnFileBrowser.setObjectName("btnFileBrowser")
        self.lblTotalFiles = QtWidgets.QLabel(self.tabFile)
        self.lblTotalFiles.setGeometry(QtCore.QRect(315, 126, 61, 16))
        self.lblTotalFiles.setObjectName("lblTotalFiles")
        self.lstFileList = QtWidgets.QListWidget(self.tabFile)
        self.lstFileList.setGeometry(QtCore.QRect(10, 10, 291, 131))
        self.lstFileList.setObjectName("lstFileList")
        self.btnClearList = QtWidgets.QPushButton(self.tabFile)
        self.btnClearList.setGeometry(QtCore.QRect(315, 32, 61, 17))
        self.btnClearList.setObjectName("btnClearList")
        self.btnMoveUpFile = QtWidgets.QPushButton(self.tabFile)
        self.btnMoveUpFile.setGeometry(QtCore.QRect(315, 87, 61, 17))
        self.btnMoveUpFile.setObjectName("btnMoveUpFile")
        self.btnDeleteFile = QtWidgets.QPushButton(self.tabFile)
        self.btnDeleteFile.setGeometry(QtCore.QRect(315, 108, 61, 17))
        self.btnDeleteFile.setObjectName("btnDeleteFile")
        self.tabWidget.addTab(self.tabFile, "")
        self.tabAdvance = QtWidgets.QWidget()
        self.tabAdvance.setObjectName("tabAdvance")
        self.tbxAdvanceCmd = QtWidgets.QPlainTextEdit(self.tabAdvance)
        self.tbxAdvanceCmd.setGeometry(QtCore.QRect(8, 20, 370, 30))
        self.tbxAdvanceCmd.setObjectName("tbxAdvanceCmd")
        self.lblAdvanceCmd = QtWidgets.QLabel(self.tabAdvance)
        self.lblAdvanceCmd.setGeometry(QtCore.QRect(10, 5, 81, 14))
        self.lblAdvanceCmd.setObjectName("lblAdvanceCmd")
        self.btnAdvanceRun = QtWidgets.QPushButton(self.tabAdvance)
        self.btnAdvanceRun.setGeometry(QtCore.QRect(320, 3, 56, 14))
        self.btnAdvanceRun.setObjectName("btnAdvanceRun")
        self.txeAdvanceOutput = QtWidgets.QTextEdit(self.tabAdvance)
        self.txeAdvanceOutput.setGeometry(QtCore.QRect(8, 53, 370, 90))
        self.txeAdvanceOutput.setReadOnly(True)
        self.txeAdvanceOutput.setObjectName("txeAdvanceOutput")
        self.tabWidget.addTab(self.tabAdvance, "")
        self.tabAbout = QtWidgets.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.tbrAbout = QtWidgets.QTextBrowser(self.tabAbout)
        self.tbrAbout.setGeometry(QtCore.QRect(10, 10, 361, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbrAbout.sizePolicy().hasHeightForWidth())
        self.tbrAbout.setSizePolicy(sizePolicy)
        self.tbrAbout.setOpenExternalLinks(True)
        self.tbrAbout.setObjectName("tbrAbout")
        self.tabWidget.addTab(self.tabAbout, "")
        winMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(winMain)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def retranslateUi(self, winMain):
        _translate = QtCore.QCoreApplication.translate
        winMain.setWindowTitle(_translate("winMain", "QffmpegUI"))
        self.btnFileBrowser.setText(_translate("winMain", "Add Files"))
        self.lblTotalFiles.setText(_translate("winMain", "0 files selected."))
        self.btnClearList.setText(_translate("winMain", "Clear List"))
        self.btnMoveUpFile.setText(_translate("winMain", "Move Up"))
        self.btnDeleteFile.setText(_translate("winMain", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFile), _translate("winMain", "File"))
        self.tbxAdvanceCmd.setPlainText(_translate("winMain", "ffmpeg -version"))
        self.lblAdvanceCmd.setText(_translate("winMain", "Advance Command"))
        self.btnAdvanceRun.setText(_translate("winMain", "Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAdvance), _translate("winMain", "Advance"))
        self.tbrAbout.setHtml(_translate("winMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff5500;\">QffmpegUI</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Version beta</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Update in April 2020</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">An opensource GUI tool developed under Python to deliver FFmpeg features.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">-----</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Repo: <a href=\"https://github.com/wklchris/QffmpegUI\"><span style=\" text-decoration: underline; color:#0000ff;\">wklchris/QffmpegUI</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License: LGPL v2.1</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAbout), _translate("winMain", "About"))
