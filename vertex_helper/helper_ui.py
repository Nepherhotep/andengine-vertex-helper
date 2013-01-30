# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helper.ui'
#
# Created: Wed Jan 30 12:08:37 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(814, 508)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphicsView = MyGraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(363, 243))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.fixtureChooser = QtGui.QComboBox(self.centralwidget)
        self.fixtureChooser.setObjectName(_fromUtf8("fixtureChooser"))
        self.verticalLayout_4.addWidget(self.fixtureChooser)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_4.addWidget(self.plainTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.patternLabel = QtGui.QLabel(self.centralwidget)
        self.patternLabel.setObjectName(_fromUtf8("patternLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.patternLabel)
        self.patternLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.patternLineEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.patternLineEdit.setObjectName(_fromUtf8("patternLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.patternLineEdit)
        self.sortClockwiseLabel = QtGui.QLabel(self.centralwidget)
        self.sortClockwiseLabel.setObjectName(_fromUtf8("sortClockwiseLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.sortClockwiseLabel)
        self.sortClockwiseCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.sortClockwiseCheckBox.setChecked(True)
        self.sortClockwiseCheckBox.setObjectName(_fromUtf8("sortClockwiseCheckBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sortClockwiseCheckBox)
        self.invertedYLabel = QtGui.QLabel(self.centralwidget)
        self.invertedYLabel.setObjectName(_fromUtf8("invertedYLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.invertedYLabel)
        self.invertedYCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.invertedYCheckBox.setObjectName(_fromUtf8("invertedYCheckBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.invertedYCheckBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionDelete_selected = QtGui.QAction(MainWindow)
        self.actionDelete_selected.setObjectName(_fromUtf8("actionDelete_selected"))
        self.actionMove_up = QtGui.QAction(MainWindow)
        self.actionMove_up.setObjectName(_fromUtf8("actionMove_up"))
        self.actionMove_down = QtGui.QAction(MainWindow)
        self.actionMove_down.setObjectName(_fromUtf8("actionMove_down"))
        self.actionMove_left = QtGui.QAction(MainWindow)
        self.actionMove_left.setObjectName(_fromUtf8("actionMove_left"))
        self.actionMove_right = QtGui.QAction(MainWindow)
        self.actionMove_right.setObjectName(_fromUtf8("actionMove_right"))
        self.actionZoom_In = QtGui.QAction(MainWindow)
        self.actionZoom_In.setObjectName(_fromUtf8("actionZoom_In"))
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        self.actionZoom_Out.setObjectName(_fromUtf8("actionZoom_Out"))
        self.menuFile.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionDelete_selected)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionMove_up)
        self.menuEdit.addAction(self.actionMove_down)
        self.menuEdit.addAction(self.actionMove_left)
        self.menuEdit.addAction(self.actionMove_right)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Andengine Vertex Helper", None))
        self.patternLabel.setText(_translate("MainWindow", "Pattern", None))
        self.sortClockwiseLabel.setText(_translate("MainWindow", "Sort Clockwise", None))
        self.invertedYLabel.setText(_translate("MainWindow", "Inverted Y", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionDelete_selected.setText(_translate("MainWindow", "Delete selected", None))
        self.actionDelete_selected.setShortcut(_translate("MainWindow", "Del", None))
        self.actionMove_up.setText(_translate("MainWindow", "Move up", None))
        self.actionMove_up.setShortcut(_translate("MainWindow", "Ctrl+Up", None))
        self.actionMove_down.setText(_translate("MainWindow", "Move down", None))
        self.actionMove_down.setShortcut(_translate("MainWindow", "Ctrl+Down", None))
        self.actionMove_left.setText(_translate("MainWindow", "Move left", None))
        self.actionMove_left.setShortcut(_translate("MainWindow", "Ctrl+Left", None))
        self.actionMove_right.setText(_translate("MainWindow", "Move right", None))
        self.actionMove_right.setShortcut(_translate("MainWindow", "Ctrl+Right", None))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In", None))
        self.actionZoom_In.setShortcut(_translate("MainWindow", "+", None))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out", None))
        self.actionZoom_Out.setShortcut(_translate("MainWindow", "-", None))

from graphicsview import MyGraphicsView
