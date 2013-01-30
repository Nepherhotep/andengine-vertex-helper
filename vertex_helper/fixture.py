'''
Created on 2011.06.05.

@author: turia
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import cmath
from conf import load as loadconf

class Fixture():
    def __init__(self, graphicsView, idNumber=0):
        self.idNumber = idNumber
        self.conf = loadconf()
        self.items = []
        self.lines = []
        self.graphicsView = graphicsView
        
    def addVertex(self, x, y):
        self.addVertexOnly(x, y)
        self.redrawOutline()
        
    def removeVertex(self,item):
        self.items.remove(item)
        self.graphicsView.scene.removeItem(item)
        
    def clearItems(self):
        for v in self.itemsSorted()[:]:
            self.removeVertex(v)
            pass
        
        self.redrawOutline()
        
    def addVertexOnly(self, x, y):
        item = QGraphicsRectItem(QRectF(0,0,10,10))
        x -=  item.rect().width() / 2
        y -=  item.rect().width() / 2
        item.setX(x )
        item.setY(y )
        item.type = 'vertex'
        self.graphicsView.selected = item
        self.graphicsView.scene.addItem(item)
        self.items.append(item)
        

    def redrawOutline(self):
        for it in self.lines[:]:
            self.graphicsView.scene.removeItem(it)
            self.lines.remove(it)
        
        if hasattr(self,'centerText') and self.centerText:
            self.graphicsView.scene.removeItem(self.centerText)
            self.centerText = None
            


        pen = QPen()
        pen.setBrush(QColor(0, 0, 0))

        verts = self.itemsSorted()
        if verts:
            halfWidth, halfHeight = self.getHalfSizes(verts[0]) 
            
            self.centerText = self.graphicsView.scene.addSimpleText(str(self.idNumber))
            x, y = self.getFixtureCenter()
            self.centerText.setX(x-self.centerText.boundingRect().width()/2)
            self.centerText.setY(y-self.centerText.boundingRect().height()/2)
        
            for i in range(len(verts)):
                line = self.graphicsView.scene.addLine(verts[i-1].x()+halfWidth,verts[i-1].y()+halfHeight, verts[i].x()+halfWidth, verts[i].y()+halfHeight,pen)
                self.lines.append(line)
                    
    def getHalfSizes(self, vertex):
        halfWidth = vertex.rect().width() / 2
        halfHeight = vertex.rect().height() / 2
        return halfWidth, halfHeight    
        
        
    def itemsSorted(self):
        vertices = self.items
        return sorted(vertices, key=self.getPhase, reverse=not self.conf['sort_clockwise'])
    
    def getPhase(self, vertex):
        centerX, centerY = self.getFixtureCenter()
            
        x, y = self.globToLocal(vertex.x(), vertex.y(),centerX,centerY)
        return cmath.phase(complex(x, y))
        
    
    def getFixtureCenter(self):
        centerOfFixtureX = 0
        centerOfFixtureY = 0
        for item in self.items:
            halfWidth, halfHeight = self.getHalfSizes(item)
            centerOfFixtureX += item.x() + halfWidth
            centerOfFixtureY += item.y() + halfHeight
        
        centerOfFixtureX /= len(self.items)
        centerOfFixtureY /= len(self.items)
        
        return centerOfFixtureX, centerOfFixtureY
        
    def center(self):
        return self.graphicsView.center()

    def globToLocal(self, x1, y1, x0=False, y0=False):
        if x0 == False:
            x0 = self.center().x()
        
        if y0 == False:
            y0 = self.center().y()
            
        x = (x1 - x0) / self.graphicsView.mainSprite.pixmap().width()
        y = (y0 - y1) / self.graphicsView.mainSprite.pixmap().height()
        if self.conf['inverted_y']:
            return (x, -y)
        else:
            return (x, y)
    
