# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Qt/ui_large.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setMinimumSize(QtCore.QSize(300, 300))
        self.mdiArea.setMaximumSize(QtCore.QSize(1920, 1080))
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(701, 141))
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
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(150, 315))
        self.dockWidget_2.setBaseSize(QtCore.QSize(0, 0))
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(100, 150))
        self.treeWidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
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
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setDefaultSectionSize(50)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setMinimumSectionSize(50)
        self.treeWidget.header().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_3.sizePolicy().hasHeightForWidth())
        self.dockWidget_3.setSizePolicy(sizePolicy)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(920, 211))
        self.dockWidget_3.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_3.setAllowedAreas(QtCore.Qt.TopDockWidgetArea)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.dockWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(721, 171))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(11, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(170, 180))
        self.widget.setObjectName("widget")
        self.lcdTime = QtWidgets.QLCDNumber(self.widget)
        self.lcdTime.setGeometry(QtCore.QRect(0, 0, 141, 41))
        self.lcdTime.setSmallDecimalPoint(False)
        self.lcdTime.setDigitCount(8)
        self.lcdTime.setProperty("value", 0.0)
        self.lcdTime.setProperty("intValue", 0)
        self.lcdTime.setObjectName("lcdTime")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(0, 45, 71, 81))
        self.groupBox.setObjectName("groupBox")
        self.btn_Start_In = QtWidgets.QPushButton(self.groupBox)
        self.btn_Start_In.setGeometry(QtCore.QRect(10, 15, 51, 23))
        self.btn_Start_In.setAutoFillBackground(False)
        self.btn_Start_In.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}")
        self.btn_Start_In.setObjectName("btn_Start_In")
        self.btn_ManTrig_In = QtWidgets.QPushButton(self.groupBox)
        self.btn_ManTrig_In.setGeometry(QtCore.QRect(10, 55, 51, 23))
        self.btn_ManTrig_In.setAutoFillBackground(False)
        self.btn_ManTrig_In.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}")
        self.btn_ManTrig_In.setObjectName("btn_ManTrig_In")
        self.btn_Stop_In = QtWidgets.QPushButton(self.groupBox)
        self.btn_Stop_In.setGeometry(QtCore.QRect(10, 35, 51, 23))
        self.btn_Stop_In.setAutoFillBackground(False)
        self.btn_Stop_In.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}")
        self.btn_Stop_In.setObjectName("btn_Stop_In")
        self.btn_InstRst = QtWidgets.QPushButton(self.widget)
        self.btn_InstRst.setGeometry(QtCore.QRect(90, 130, 71, 41))
        self.btn_InstRst.setAutoFillBackground(False)
        self.btn_InstRst.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}")
        self.btn_InstRst.setObjectName("btn_InstRst")
        self.btn_ManTrig = QtWidgets.QPushButton(self.widget)
        self.btn_ManTrig.setGeometry(QtCore.QRect(0, 130, 71, 41))
        self.btn_ManTrig.setObjectName("btn_ManTrig")
        self.horizontalLayout_3.addWidget(self.widget)
        self.tbl_Instruments = QtWidgets.QTableWidget(self.widget_2)
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
        self.tbl_Instruments.setToolTip("")
        self.tbl_Instruments.setAutoFillBackground(False)
        self.tbl_Instruments.setStyleSheet("QProgressBar::chunk {background-color: #3add36; width: 1px;}\n"
"section::{font: 12px;}")
        self.tbl_Instruments.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tbl_Instruments.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tbl_Instruments.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_Instruments.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_Instruments.setAlternatingRowColors(True)
        self.tbl_Instruments.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_Instruments.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_Instruments.setRowCount(0)
        self.tbl_Instruments.setColumnCount(4)
        self.tbl_Instruments.setObjectName("tbl_Instruments")
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Instruments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Instruments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Instruments.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Instruments.setHorizontalHeaderItem(3, item)
        self.tbl_Instruments.horizontalHeader().setDefaultSectionSize(72)
        self.tbl_Instruments.horizontalHeader().setMinimumSectionSize(18)
        self.tbl_Instruments.verticalHeader().setVisible(False)
        self.tbl_Instruments.verticalHeader().setDefaultSectionSize(25)
        self.tbl_Instruments.verticalHeader().setHighlightSections(False)
        self.tbl_Instruments.verticalHeader().setSortIndicatorShown(False)
        self.tbl_Instruments.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_3.addWidget(self.tbl_Instruments)
        self.horizontalLayout.addWidget(self.widget_2)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Master Log"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Status Info..."))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Connections & Events"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Signal"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Last Value"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Direct Connections"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Events"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.dockWidget_3.setWindowTitle(_translate("MainWindow", "Instrument Control"))
        self.groupBox.setTitle(_translate("MainWindow", "Inst. Trigger"))
        self.btn_Start_In.setText(_translate("MainWindow", "Start"))
        self.btn_ManTrig_In.setText(_translate("MainWindow", "Manual"))
        self.btn_Stop_In.setText(_translate("MainWindow", "Stop"))
        self.btn_InstRst.setText(_translate("MainWindow", "Reset\n"
"Instrument"))
        self.btn_ManTrig.setText(_translate("MainWindow", "Global\n"
"Trigger"))
        item = self.tbl_Instruments.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Instrument"))
        item = self.tbl_Instruments.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Acq#"))
        item = self.tbl_Instruments.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tbl_Instruments.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data Path"))

