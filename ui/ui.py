# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Qt/ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 321, 241))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 60, 291, 151))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.plainTextEdit.setPalette(palette)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setDocumentTitle("")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlaceholderText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lcdTime = QtWidgets.QLCDNumber(self.tab)
        self.lcdTime.setGeometry(QtCore.QRect(10, 10, 131, 41))
        self.lcdTime.setSmallDecimalPoint(False)
        self.lcdTime.setDigitCount(8)
        self.lcdTime.setProperty("value", 0.0)
        self.lcdTime.setProperty("intValue", 0)
        self.lcdTime.setObjectName("lcdTime")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.btn_ManTrig = QtWidgets.QPushButton(self.tab_3)
        self.btn_ManTrig.setGeometry(QtCore.QRect(80, 90, 51, 41))
        self.btn_ManTrig.setObjectName("btn_ManTrig")
        self.txt_InstStat = QtWidgets.QPlainTextEdit(self.tab_3)
        self.txt_InstStat.setGeometry(QtCore.QRect(80, 135, 231, 76))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txt_InstStat.setPalette(palette)
        self.txt_InstStat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_InstStat.setDocumentTitle("")
        self.txt_InstStat.setReadOnly(True)
        self.txt_InstStat.setPlaceholderText("")
        self.txt_InstStat.setObjectName("txt_InstStat")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(5, 90, 71, 121))
        self.groupBox.setObjectName("groupBox")
        self.btn_InstRst = QtWidgets.QPushButton(self.groupBox)
        self.btn_InstRst.setGeometry(QtCore.QRect(10, 90, 51, 23))
        self.btn_InstRst.setAutoFillBackground(False)
        self.btn_InstRst.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}")
        self.btn_InstRst.setObjectName("btn_InstRst")
        self.btn_Start_In = QtWidgets.QPushButton(self.groupBox)
        self.btn_Start_In.setGeometry(QtCore.QRect(10, 20, 51, 23))
        self.btn_Start_In.setAutoFillBackground(False)
        self.btn_Start_In.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}")
        self.btn_Start_In.setObjectName("btn_Start_In")
        self.btn_ManTrig_In = QtWidgets.QPushButton(self.groupBox)
        self.btn_ManTrig_In.setGeometry(QtCore.QRect(10, 60, 51, 23))
        self.btn_ManTrig_In.setAutoFillBackground(False)
        self.btn_ManTrig_In.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}")
        self.btn_ManTrig_In.setObjectName("btn_ManTrig_In")
        self.btn_Stop_In = QtWidgets.QPushButton(self.groupBox)
        self.btn_Stop_In.setGeometry(QtCore.QRect(10, 40, 51, 23))
        self.btn_Stop_In.setAutoFillBackground(False)
        self.btn_Stop_In.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}")
        self.btn_Stop_In.setObjectName("btn_Stop_In")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 90, 291, 121))
        self.stackedWidget.setObjectName("stackedWidget")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.stackedWidget_log = QtWidgets.QStackedWidget(self.tab_4)
        self.stackedWidget_log.setGeometry(QtCore.QRect(10, 90, 291, 121))
        self.stackedWidget_log.setObjectName("stackedWidget_log")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_5)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 291, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setDefaultSectionSize(200)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(20)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.treeWidget.header().setStretchLastSection(True)
        self.tabWidget.addTab(self.tab_5, "")
        self.tbl_Instruments = QtWidgets.QTableWidget(self.centralWidget)
        self.tbl_Instruments.setGeometry(QtCore.QRect(0, 25, 321, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.tbl_Instruments.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tbl_Instruments.setFont(font)
        self.tbl_Instruments.setAutoFillBackground(False)
        self.tbl_Instruments.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}")
        self.tbl_Instruments.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tbl_Instruments.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tbl_Instruments.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_Instruments.setAlternatingRowColors(True)
        self.tbl_Instruments.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_Instruments.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_Instruments.setRowCount(0)
        self.tbl_Instruments.setColumnCount(3)
        self.tbl_Instruments.setObjectName("tbl_Instruments")
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Instruments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Instruments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Instruments.setHorizontalHeaderItem(2, item)
        self.tbl_Instruments.horizontalHeader().setDefaultSectionSize(72)
        self.tbl_Instruments.horizontalHeader().setMinimumSectionSize(18)
        self.tbl_Instruments.verticalHeader().setVisible(False)
        self.tbl_Instruments.verticalHeader().setDefaultSectionSize(25)
        self.tbl_Instruments.verticalHeader().setHighlightSections(False)
        self.tbl_Instruments.verticalHeader().setSortIndicatorShown(False)
        self.tbl_Instruments.verticalHeader().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Mstr Log"))
        self.btn_ManTrig.setText(_translate("MainWindow", "Global\n"
"Trigger"))
        self.groupBox.setTitle(_translate("MainWindow", "Individual"))
        self.btn_InstRst.setText(_translate("MainWindow", "Reset"))
        self.btn_Start_In.setText(_translate("MainWindow", "Start"))
        self.btn_ManTrig_In.setText(_translate("MainWindow", "Manual"))
        self.btn_Stop_In.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Triggers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Inst"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Inst Logs"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Signal"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Last Value"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Direct Connections"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Events"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Events"))
        item = self.tbl_Instruments.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Instrument"))
        item = self.tbl_Instruments.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Acq#"))
        item = self.tbl_Instruments.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))

