# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twitterbot.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormTwitterBot(object):
    def setupUi(self, FormTwitterBot):
        FormTwitterBot.setObjectName("FormTwitterBot")
        FormTwitterBot.resize(1056, 699)
        self.widget_BotLaunch = QtWidgets.QWidget(FormTwitterBot)
        self.widget_BotLaunch.setGeometry(QtCore.QRect(0, 0, 671, 351))
        self.widget_BotLaunch.setObjectName("widget_BotLaunch")
        self.Lbl_BotPubFreq = QtWidgets.QLabel(self.widget_BotLaunch)
        self.Lbl_BotPubFreq.setGeometry(QtCore.QRect(52, 79, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lbl_BotPubFreq.setFont(font)
        self.Lbl_BotPubFreq.setObjectName("Lbl_BotPubFreq")
        self.Lbl_BotRepTime = QtWidgets.QLabel(self.widget_BotLaunch)
        self.Lbl_BotRepTime.setGeometry(QtCore.QRect(49, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lbl_BotRepTime.setFont(font)
        self.Lbl_BotRepTime.setObjectName("Lbl_BotRepTime")
        self.Lbl_BotRepEmail = QtWidgets.QLabel(self.widget_BotLaunch)
        self.Lbl_BotRepEmail.setGeometry(QtCore.QRect(50, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lbl_BotRepEmail.setFont(font)
        self.Lbl_BotRepEmail.setObjectName("Lbl_BotRepEmail")
        self.Lbl_BotStatByEmail = QtWidgets.QLabel(self.widget_BotLaunch)
        self.Lbl_BotStatByEmail.setGeometry(QtCore.QRect(50, 240, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lbl_BotStatByEmail.setFont(font)
        self.Lbl_BotStatByEmail.setObjectName("Lbl_BotStatByEmail")
        self.pTE_BotPubFreq = QtWidgets.QPlainTextEdit(self.widget_BotLaunch)
        self.pTE_BotPubFreq.setGeometry(QtCore.QRect(220, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pTE_BotPubFreq.setFont(font)
        self.pTE_BotPubFreq.setObjectName("pTE_BotPubFreq")
        self.pTE_BotRepEmail = QtWidgets.QPlainTextEdit(self.widget_BotLaunch)
        self.pTE_BotRepEmail.setGeometry(QtCore.QRect(220, 160, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pTE_BotRepEmail.setFont(font)
        self.pTE_BotRepEmail.setObjectName("pTE_BotRepEmail")
        self.pB_BotLdFile = QtWidgets.QPushButton(self.widget_BotLaunch)
        self.pB_BotLdFile.setGeometry(QtCore.QRect(40, 310, 111, 28))
        self.pB_BotLdFile.setObjectName("pB_BotLdFile")
        self.pB_BotDestroy = QtWidgets.QPushButton(self.widget_BotLaunch)
        self.pB_BotDestroy.setGeometry(QtCore.QRect(410, 240, 111, 28))
        self.pB_BotDestroy.setObjectName("pB_BotDestroy")
        self.pB_BotEditFile = QtWidgets.QPushButton(self.widget_BotLaunch)
        self.pB_BotEditFile.setGeometry(QtCore.QRect(290, 310, 111, 28))
        self.pB_BotEditFile.setObjectName("pB_BotEditFile")
        self.pB_BotSaveFile = QtWidgets.QPushButton(self.widget_BotLaunch)
        self.pB_BotSaveFile.setGeometry(QtCore.QRect(160, 310, 121, 28))
        self.pB_BotSaveFile.setObjectName("pB_BotSaveFile")
        self.Lbl_BotFileName = QtWidgets.QLabel(self.widget_BotLaunch)
        self.Lbl_BotFileName.setGeometry(QtCore.QRect(52, 39, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lbl_BotFileName.setFont(font)
        self.Lbl_BotFileName.setObjectName("Lbl_BotFileName")
        self.pTE_BotFileName = QtWidgets.QPlainTextEdit(self.widget_BotLaunch)
        self.pTE_BotFileName.setEnabled(True)
        self.pTE_BotFileName.setGeometry(QtCore.QRect(220, 40, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pTE_BotFileName.setFont(font)
        self.pTE_BotFileName.setObjectName("pTE_BotFileName")
        self.Lbl_BotTTLocal = QtWidgets.QLabel(self.widget_BotLaunch)
        self.Lbl_BotTTLocal.setGeometry(QtCore.QRect(50, 200, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lbl_BotTTLocal.setFont(font)
        self.Lbl_BotTTLocal.setObjectName("Lbl_BotTTLocal")
        self.ckBoxBotStatByEmail = QtWidgets.QCheckBox(self.widget_BotLaunch)
        self.ckBoxBotStatByEmail.setGeometry(QtCore.QRect(245, 246, 81, 20))
        self.ckBoxBotStatByEmail.setText("")
        self.ckBoxBotStatByEmail.setObjectName("ckBoxBotStatByEmail")
        self.pB_BotExecute = QtWidgets.QPushButton(self.widget_BotLaunch)
        self.pB_BotExecute.setGeometry(QtCore.QRect(280, 240, 121, 28))
        self.pB_BotExecute.setObjectName("pB_BotExecute")
        self.cBox_BotTTLocal = QtWidgets.QComboBox(self.widget_BotLaunch)
        self.cBox_BotTTLocal.setGeometry(QtCore.QRect(220, 200, 321, 31))
        self.cBox_BotTTLocal.setObjectName("cBox_BotTTLocal")
        self.dSB_BotRepTim = QtWidgets.QDoubleSpinBox(self.widget_BotLaunch)
        self.dSB_BotRepTim.setGeometry(QtCore.QRect(220, 120, 71, 31))
        self.dSB_BotRepTim.setDecimals(0)
        self.dSB_BotRepTim.setMaximum(10.0)
        self.dSB_BotRepTim.setObjectName("dSB_BotRepTim")
        self.pB_BotClose = QtWidgets.QPushButton(self.widget_BotLaunch)
        self.pB_BotClose.setGeometry(QtCore.QRect(540, 310, 121, 28))
        self.pB_BotClose.setObjectName("pB_BotClose")
        self.widget_StatusBar = QtWidgets.QWidget(self.widget_BotLaunch)
        self.widget_StatusBar.setGeometry(QtCore.QRect(89, 275, 541, 30))
        self.widget_StatusBar.setObjectName("widget_StatusBar")
        self.lbl_DestroyingStatuses = QtWidgets.QLabel(self.widget_StatusBar)
        self.lbl_DestroyingStatuses.setGeometry(QtCore.QRect(40, 0, 131, 20))
        self.lbl_DestroyingStatuses.setObjectName("lbl_DestroyingStatuses")
        self.pBarDestroyingStatuses = QtWidgets.QProgressBar(self.widget_StatusBar)
        self.pBarDestroyingStatuses.setGeometry(QtCore.QRect(180, 0, 341, 23))
        self.pBarDestroyingStatuses.setProperty("value", 0)
        self.pBarDestroyingStatuses.setFormat("")
        self.pBarDestroyingStatuses.setObjectName("pBarDestroyingStatuses")
        self.Lbl_BotEdit = QtWidgets.QLabel(FormTwitterBot)
        self.Lbl_BotEdit.setGeometry(QtCore.QRect(30, 380, 111, 16))
        self.Lbl_BotEdit.setObjectName("Lbl_BotEdit")
        self.pTE_BotFileEditt = QtWidgets.QPlainTextEdit(FormTwitterBot)
        self.pTE_BotFileEditt.setGeometry(QtCore.QRect(30, 400, 1001, 281))
        self.pTE_BotFileEditt.setObjectName("pTE_BotFileEditt")
        self.label = QtWidgets.QLabel(FormTwitterBot)
        self.label.setGeometry(QtCore.QRect(690, 210, 91, 10))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormTwitterBot)
        self.label_2.setGeometry(QtCore.QRect(690, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.lW_GlobalTrending = QtWidgets.QListWidget(FormTwitterBot)
        self.lW_GlobalTrending.setGeometry(QtCore.QRect(790, 10, 256, 192))
        self.lW_GlobalTrending.setObjectName("lW_GlobalTrending")
        self.lW_LocalTrending = QtWidgets.QListWidget(FormTwitterBot)
        self.lW_LocalTrending.setGeometry(QtCore.QRect(790, 205, 256, 192))
        self.lW_LocalTrending.setObjectName("lW_LocalTrending")

        self.retranslateUi(FormTwitterBot)
        QtCore.QMetaObject.connectSlotsByName(FormTwitterBot)

    def retranslateUi(self, FormTwitterBot):
        _translate = QtCore.QCoreApplication.translate
        FormTwitterBot.setWindowTitle(_translate("FormTwitterBot", "Twitter Bot"))
        self.Lbl_BotPubFreq.setText(_translate("FormTwitterBot", "Publish Time Freq."))
        self.Lbl_BotRepTime.setText(_translate("FormTwitterBot", "Repeat Times"))
        self.Lbl_BotRepEmail.setText(_translate("FormTwitterBot", "Reporting email"))
        self.Lbl_BotStatByEmail.setText(_translate("FormTwitterBot", "Report Statuses by eMail"))
        self.pB_BotLdFile.setText(_translate("FormTwitterBot", "Load Bot File"))
        self.pB_BotDestroy.setText(_translate("FormTwitterBot", "Destroy Statuses"))
        self.pB_BotEditFile.setText(_translate("FormTwitterBot", "Edit with External"))
        self.pB_BotSaveFile.setText(_translate("FormTwitterBot", "Save Bot File"))
        self.Lbl_BotFileName.setText(_translate("FormTwitterBot", "Bot File Name"))
        self.Lbl_BotTTLocal.setText(_translate("FormTwitterBot", "Trending Topic local"))
        self.pB_BotExecute.setText(_translate("FormTwitterBot", "Execute Bot"))
        self.pB_BotClose.setText(_translate("FormTwitterBot", "Close"))
        self.lbl_DestroyingStatuses.setText(_translate("FormTwitterBot", "Destroying Statuses"))
        self.Lbl_BotEdit.setText(_translate("FormTwitterBot", "Bot File Quick View"))
        self.label.setText(_translate("FormTwitterBot", "Local Trending"))
        self.label_2.setText(_translate("FormTwitterBot", "Global Trending"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormTwitterBot = QtWidgets.QWidget()
    ui = Ui_FormTwitterBot()
    ui.setupUi(FormTwitterBot)
    FormTwitterBot.show()
    sys.exit(app.exec_())
