# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created: Tue Aug 12 20:56:52 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1168, 805)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("*{\n"
"font-family:\"Courier New\", Times, serif;\n"
"}\n"
"QPushButton {\n"
"background-color: white;\n"
"color: black;\n"
"padding: 5px;\n"
"border: 1px solid transparent;\n"
"border-color: #ccc;\n"
"border-radius: 4px;\n"
"font-family: \"sans-serif\", Times, serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #00CCCC;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #0066CC;\n"
"border-color: yellow;\n"
"}\n"
"\n"
"QComboBox {\n"
"background-color: #CCCCCC;\n"
"color: black;\n"
"padding: 5px;\n"
"font-family:\"Courier New\", Times, serif;\n"
"border: 1px solid transparent;\n"
"border-color: #ccc;\n"
"}"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.cbDevice = QtGui.QComboBox(Dialog)
        self.cbDevice.setEditable(False)
        self.cbDevice.setObjectName(_fromUtf8("cbDevice"))
        self.cbDevice.addItem(_fromUtf8(""))
        self.cbDevice.addItem(_fromUtf8(""))
        self.cbDevice.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.cbDevice)
        self.cbPhoneno = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbPhoneno.sizePolicy().hasHeightForWidth())
        self.cbPhoneno.setSizePolicy(sizePolicy)
        self.cbPhoneno.setMinimumSize(QtCore.QSize(200, 25))
        self.cbPhoneno.setMaximumSize(QtCore.QSize(200, 26))
        self.cbPhoneno.setStyleSheet(_fromUtf8("background-color: white; color: black;"))
        self.cbPhoneno.setEditable(True)
        self.cbPhoneno.setObjectName(_fromUtf8("cbPhoneno"))
        self.horizontalLayout_5.addWidget(self.cbPhoneno)
        self.btnConnect = QtGui.QPushButton(Dialog)
        self.btnConnect.setStyleSheet(_fromUtf8(""))
        self.btnConnect.setObjectName(_fromUtf8("btnConnect"))
        self.horizontalLayout_5.addWidget(self.btnConnect)
        self.btnRefresh = QtGui.QPushButton(Dialog)
        self.btnRefresh.setObjectName(_fromUtf8("btnRefresh"))
        self.horizontalLayout_5.addWidget(self.btnRefresh)
        self.btnRestart = QtGui.QPushButton(Dialog)
        self.btnRestart.setObjectName(_fromUtf8("btnRestart"))
        self.horizontalLayout_5.addWidget(self.btnRestart)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_7.addWidget(self.line)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.btnSelectDir = QtGui.QPushButton(Dialog)
        self.btnSelectDir.setObjectName(_fromUtf8("btnSelectDir"))
        self.horizontalLayout_7.addWidget(self.btnSelectDir)
        self.leWorkspace = QtGui.QLineEdit(Dialog)
        self.leWorkspace.setObjectName(_fromUtf8("leWorkspace"))
        self.horizontalLayout_7.addWidget(self.leWorkspace)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.cbDestdir = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDestdir.sizePolicy().hasHeightForWidth())
        self.cbDestdir.setSizePolicy(sizePolicy)
        self.cbDestdir.setMinimumSize(QtCore.QSize(120, 0))
        self.cbDestdir.setObjectName(_fromUtf8("cbDestdir"))
        self.cbDestdir.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.cbDestdir)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.widget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(500, 0))
        self.widget.setMaximumSize(QtCore.QSize(1000000, 16777215))
        self.widget.setStyleSheet(_fromUtf8("QWidget{\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color:black;\n"
"}"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.lblScreen = QtGui.QLabel(self.widget)
        self.lblScreen.setGeometry(QtCore.QRect(0, 0, 0, 0))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblScreen.sizePolicy().hasHeightForWidth())
        self.lblScreen.setSizePolicy(sizePolicy)
        self.lblScreen.setMinimumSize(QtCore.QSize(0, 0))
        self.lblScreen.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lblScreen.setMouseTracking(True)
        self.lblScreen.setStyleSheet(_fromUtf8("QLabel{\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color:green;\n"
"}"))
        self.lblScreen.setFrameShadow(QtGui.QFrame.Raised)
        self.lblScreen.setLineWidth(200)
        self.lblScreen.setMidLineWidth(500)
        self.lblScreen.setText(_fromUtf8(""))
        self.lblScreen.setScaledContents(True)
        self.lblScreen.setObjectName(_fromUtf8("lblScreen"))
        self.verticalLayout_5.addWidget(self.widget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_6.addWidget(self.line_4)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_6.addWidget(self.line_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.leCode = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leCode.sizePolicy().hasHeightForWidth())
        self.leCode.setSizePolicy(sizePolicy)
        self.leCode.setMinimumSize(QtCore.QSize(330, 0))
        self.leCode.setObjectName(_fromUtf8("leCode"))
        self.horizontalLayout_8.addWidget(self.leCode)
        self.btnRun = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRun.sizePolicy().hasHeightForWidth())
        self.btnRun.setSizePolicy(sizePolicy)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.horizontalLayout_8.addWidget(self.btnRun)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.line_7 = QtGui.QFrame(Dialog)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_3.addWidget(self.line_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnClick = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClick.sizePolicy().hasHeightForWidth())
        self.btnClick.setSizePolicy(sizePolicy)
        self.btnClick.setMinimumSize(QtCore.QSize(100, 0))
        self.btnClick.setObjectName(_fromUtf8("btnClick"))
        self.verticalLayout_2.addWidget(self.btnClick)
        self.btnDrag = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDrag.sizePolicy().hasHeightForWidth())
        self.btnDrag.setSizePolicy(sizePolicy)
        self.btnDrag.setMinimumSize(QtCore.QSize(100, 0))
        self.btnDrag.setObjectName(_fromUtf8("btnDrag"))
        self.verticalLayout_2.addWidget(self.btnDrag)
        self.btnWait = QtGui.QPushButton(Dialog)
        self.btnWait.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnWait.sizePolicy().hasHeightForWidth())
        self.btnWait.setSizePolicy(sizePolicy)
        self.btnWait.setMinimumSize(QtCore.QSize(100, 0))
        self.btnWait.setObjectName(_fromUtf8("btnWait"))
        self.verticalLayout_2.addWidget(self.btnWait)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnFindAll = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFindAll.sizePolicy().hasHeightForWidth())
        self.btnFindAll.setSizePolicy(sizePolicy)
        self.btnFindAll.setMinimumSize(QtCore.QSize(100, 0))
        self.btnFindAll.setObjectName(_fromUtf8("btnFindAll"))
        self.horizontalLayout_2.addWidget(self.btnFindAll)
        self.sbThreshold = QtGui.QDoubleSpinBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbThreshold.sizePolicy().hasHeightForWidth())
        self.sbThreshold.setSizePolicy(sizePolicy)
        self.sbThreshold.setDecimals(1)
        self.sbThreshold.setMaximum(1.0)
        self.sbThreshold.setSingleStep(0.1)
        self.sbThreshold.setProperty("value", 0.8)
        self.sbThreshold.setObjectName(_fromUtf8("sbThreshold"))
        self.horizontalLayout_2.addWidget(self.sbThreshold)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.leCrop1 = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leCrop1.sizePolicy().hasHeightForWidth())
        self.leCrop1.setSizePolicy(sizePolicy)
        self.leCrop1.setMinimumSize(QtCore.QSize(160, 0))
        self.leCrop1.setObjectName(_fromUtf8("leCrop1"))
        self.verticalLayout_4.addWidget(self.leCrop1)
        self.lblCutImage1 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCutImage1.sizePolicy().hasHeightForWidth())
        self.lblCutImage1.setSizePolicy(sizePolicy)
        self.lblCutImage1.setMinimumSize(QtCore.QSize(160, 100))
        self.lblCutImage1.setMaximumSize(QtCore.QSize(100, 100))
        self.lblCutImage1.setStyleSheet(_fromUtf8("QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:green;\n"
"    background-color: gray;\n"
"}"))
        self.lblCutImage1.setText(_fromUtf8(""))
        self.lblCutImage1.setObjectName(_fromUtf8("lblCutImage1"))
        self.verticalLayout_4.addWidget(self.lblCutImage1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.leCrop2 = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leCrop2.sizePolicy().hasHeightForWidth())
        self.leCrop2.setSizePolicy(sizePolicy)
        self.leCrop2.setMinimumSize(QtCore.QSize(160, 0))
        self.leCrop2.setObjectName(_fromUtf8("leCrop2"))
        self.verticalLayout_4.addWidget(self.leCrop2)
        self.lblCutImage2 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCutImage2.sizePolicy().hasHeightForWidth())
        self.lblCutImage2.setSizePolicy(sizePolicy)
        self.lblCutImage2.setMinimumSize(QtCore.QSize(160, 100))
        self.lblCutImage2.setMaximumSize(QtCore.QSize(100, 100))
        self.lblCutImage2.setStyleSheet(_fromUtf8("QLabel{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:green;\n"
"    background-color: gray;\n"
"}"))
        self.lblCutImage2.setText(_fromUtf8(""))
        self.lblCutImage2.setObjectName(_fromUtf8("lblCutImage2"))
        self.verticalLayout_4.addWidget(self.lblCutImage2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_22.addWidget(self.line_3)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_22.addWidget(self.label_5)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(300, 0))
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_22.addWidget(self.textBrowser)
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_22.addWidget(self.line_5)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.btnRunScripts = QtGui.QPushButton(Dialog)
        self.btnRunScripts.setObjectName(_fromUtf8("btnRunScripts"))
        self.horizontalLayout_12.addWidget(self.btnRunScripts)
        self.btnClear = QtGui.QPushButton(Dialog)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.horizontalLayout_12.addWidget(self.btnClear)
        self.btnSave = QtGui.QPushButton(Dialog)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout_12.addWidget(self.btnSave)
        self.verticalLayout_22.addLayout(self.horizontalLayout_12)
        self.horizontalLayout.addLayout(self.verticalLayout_22)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line_6 = QtGui.QFrame(Dialog)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setStyleSheet(_fromUtf8("*{\n"
"background-color: #ccc;\n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tbConsole = QtGui.QTextBrowser(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tbConsole.sizePolicy().hasHeightForWidth())
        self.tbConsole.setSizePolicy(sizePolicy)
        self.tbConsole.setMinimumSize(QtCore.QSize(0, 100))
        self.tbConsole.setMaximumSize(QtCore.QSize(16777215, 140))
        self.tbConsole.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tbConsole.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tbConsole.setObjectName(_fromUtf8("tbConsole"))
        self.verticalLayout_6.addWidget(self.tbConsole)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Airkuli - airtest GUI", None))
        self.cbDevice.setItemText(0, _translate("Dialog", "android", None))
        self.cbDevice.setItemText(1, _translate("Dialog", "windows", None))
        self.cbDevice.setItemText(2, _translate("Dialog", "ios", None))
        self.btnConnect.setText(_translate("Dialog", "connect", None))
        self.btnRefresh.setText(_translate("Dialog", "refresh", None))
        self.btnRestart.setText(_translate("Dialog", "restart", None))
        self.btnSelectDir.setText(_translate("Dialog", "选择文件夹", None))
        self.label_2.setText(_translate("Dialog", "目标文件夹：", None))
        self.cbDestdir.setItemText(0, _translate("Dialog", "image", None))
        self.btnRun.setText(_translate("Dialog", "运行代码", None))
        self.btnClick.setText(_translate("Dialog", "click", None))
        self.btnDrag.setText(_translate("Dialog", "drag", None))
        self.btnWait.setText(_translate("Dialog", "wait", None))
        self.btnFindAll.setText(_translate("Dialog", "findall", None))
        self.label_5.setText(_translate("Dialog", "Commands Generated", None))
        self.btnRunScripts.setText(_translate("Dialog", "Run", None))
        self.btnClear.setText(_translate("Dialog", "Clear", None))
        self.btnSave.setText(_translate("Dialog", "Save", None))
        self.label.setText(_translate("Dialog", "Status:", None))
