###############################################################################
# Encoding: UTF-8                                                             #
# Author: Alexey Zankevich <alex.zankevich@gmail.com>                         #                                      
# Copyright: (c) 2010 Alexei Zankevich <alex.zankevich@gmail.com>             #                                      
# Licence: BSD                                                                #
############################################################################### 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from conf import load as loadconf
from copy import deepcopy
from helper_ui import Ui_MainWindow
from fixture import Fixture
import re
import cmath
import json
import math
import os
import platform
import sys
import threading


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.__index = 0
        self.fixtures = []
        self.changedByProg = True
        self.setupUi(self)
        self.connectSlots()
        self.conf = loadconf()
        self.graphicsView.setMainWindow(self)
        self.patternLineEdit.setText(self.conf['pattern'])
        self.sortClockwiseCheckBox.setChecked(self.conf['sort_clockwise'])
        self.invertedYCheckBox.setChecked(self.conf['inverted_y'])
        if 'last_file' in self.conf:
            filename = self.conf['last_file']
            self.graphicsView.loadSprite(filename)
            
        self.addNewFixture()

    def chosen(self,index):
        if index == 'add new':
            self.addNewFixture()
        else:
            self.graphicsView.actFixture = self.fixtures[int(index)-1]
            if self.graphicsView.actFixture.itemsSorted():
                self.graphicsView.selected = self.graphicsView.actFixture.itemsSorted()[-1]
            else:
                self.graphicsView.selected = None
                
            self.graphicsView.actFixture.redrawOutline()
            self.updateText()
            

    def addNewFixture(self):
        newIdNumber = len(self.fixtures)+1
        fixture = Fixture(self.graphicsView, newIdNumber);
        self.fixtures.append(fixture)
        self.fixtureChooser.addItem(str(len(self.fixtures)))
        self.fixtureChooser.setCurrentIndex(len(self.fixtures))
        self.chosen(len(self.fixtures))

    def redrawFixtures(self):
        for fixture in self.fixtures:
            fixture.redrawOutline()

    def connectSlots(self):
        self.connect(self.fixtureChooser, SIGNAL('activated(QString)'),self.chosen)
        self.connect(self.actionOpen, SIGNAL('triggered()'), self.openFile)
        self.connect(self.actionDelete_selected, SIGNAL('triggered()'),
                     self.graphicsView.removeSelectedVertex)
        self.connect(self.actionMove_up, SIGNAL('triggered()'),
                     self.graphicsView.moveVertexUp)
        self.connect(self.actionMove_down, SIGNAL('triggered()'),
                     self.graphicsView.moveVertexDown)
        self.connect(self.actionMove_left, SIGNAL('triggered()'),
                     self.graphicsView.moveVertexLeft)
        self.connect(self.actionMove_right, SIGNAL('triggered()'),
                     self.graphicsView.moveVertexRight)
        self.connect(self.actionZoom_In, SIGNAL('triggered()'), self.graphicsView.zoomIn)
        self.connect(self.actionZoom_Out, SIGNAL('triggered()'), self.graphicsView.zoomOut)
        self.plainTextEdit.textChanged.connect(self.onPlainTextEditChanged)
        self.patternLineEdit.editingFinished.connect(self.onPatternEdited)
        self.sortClockwiseCheckBox.toggled.connect(self.onSortCheckBoxToggled)
        self.invertedYCheckBox.toggled.connect(self.onInvertedYCheckBoxToggled)


    def onPlainTextEditChanged(self):
        if self.changedByProg:
            self.changedByProg = False
            return
        
        text = str(self.plainTextEdit.document().toPlainText())
        textLines = text.splitlines()
        i = 0
        self.graphicsView.actFixture.clearItems()
        for textLine in textLines:
            i+=1
            m = re.match("new Vector2\(([^f]+)f\*width, ([^f]+)f\*height\)",textLine.strip())
            if m is None:
                continue
            x = m.group(1)
            y = m.group(2)
            self.graphicsView.actFixture.addVertexOnly(*self.textToSceneCoord(float(x), float(y)))
            
        self.graphicsView.actFixture.redrawOutline()
            
    def textToSceneCoord(self, locx, locy):
        x0, y0 = self.graphicsView.center().x(), self.graphicsView.center().y()
        globalx = locx * self.graphicsView.mainSprite.pixmap().width() + x0
        globaly = - locy * self.graphicsView.mainSprite.pixmap().height() + y0
        
        if self.conf['inverted_y']:
            globaly = locy * self.graphicsView.mainSprite.pixmap().height() + y0
        return (globalx, globaly)
            
    def onInvertedYCheckBoxToggled(self, checked):
        self.conf['inverted_y'] = checked
        self.conf.save()
        self.updateText()

    def onSortCheckBoxToggled(self, checked):
        self.conf['sort_clockwise'] = checked
        self.conf.save()
        self.updateText()

    def onPatternEdited(self):
        self.conf['pattern'] = unicode(self.patternLineEdit.text())
        self.conf.save()
        self.updateText()

    def openFile(self):
        dir = self.conf['sprites_dir']
        filename = QFileDialog.getOpenFileName(None, "FileDialog", dir)
        if filename:
            self.conf['sprites_dir'] = os.path.dirname(unicode(filename))
            self.conf['last_file'] = str(filename)
            self.conf.save()
            self.graphicsView.loadSprite(filename)

    def updateText(self):
        text = ''
        for item in self.graphicsView.actFixture.itemsSorted():
            pattern = unicode(self.patternLineEdit.text())
            line = pattern % tuple(self.graphicsView.actFixture.globToLocal(*self.graphicsView.getPos(item)))
            line += "\n"
            text += line
        
        if text == '':
            text = ' '

        self.changedByProg = True
        self.plainTextEdit.setPlainText(str(text))



def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
