###############################################################################
# Encoding: UTF-8                                                             #
# Author: Alexey Zankevich <alex.zankevich@gmail.com>                         #                                      
# Copyright: (c) 2010 Alexei Zankevich <alex.zankevich@gmail.com>             #                                      
# Licence: BSD                                                                #
############################################################################### 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from conf import load as loadconf
from fixture import Fixture



class MyGraphicsView(QGraphicsView):
    signalZoomByMouse = pyqtSignal()
    
    
    def __init__(self, *args, **kwargs):
        super(MyGraphicsView, self).__init__()
        scene = QGraphicsScene(self)
        self.mainWindow = args[0]
        self.actFixture = Fixture(self)
        self.conf = loadconf()
        self.scene = scene
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.setSceneRect(0, 0, self.conf['x_max'], self.conf['y_max'])
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setCacheMode(QGraphicsView.CacheNone)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.grabbed = None
        self.selected = None
        self.bgImage = None
        self.mainSprite = None
        self.zoom = 1
        self.zoomStep = 2 # used by menu commands
        self.zoomScale = 1 # used by mouse zoom
        self.signalZoomByMouse.connect(self.slotZoom,Qt.QueuedConnection)
        self.setTransformationAnchor( QGraphicsView.NoAnchor )

    def slotZoom(self):
        newMapped = QPointF(self.mapToScene(self.lastPos))
        deltaX = newMapped.x() - self.lastMapped.x()
        deltaY = newMapped.y() - self.lastMapped.y()
        self.translate(deltaX, deltaY)
        pass
    
    def wheelEvent(self, event):
        if event.modifiers() == Qt.ControlModifier:
            if event.orientation() == Qt.Vertical:
                self.lastPos = event.pos()
                self.lastMapped = QPointF(self.mapToScene(self.lastPos))
                
                if event.delta() > 0:
                    self.zoomScale *= 1.2
                    self.scale(1.2, 1.2)
                else:
                    self.zoomScale /= 1.2
                    self.scale(1/1.2, 1/1.2)
                
                self.signalZoomByMouse.emit()

        else:
            QGraphicsView.wheelEvent(self, event)
      

    def zoomIn(self):
        self.zoom *= self.zoomStep
        self.scale(self.zoomStep, self.zoomStep)

    def zoomOut(self):
        self.zoom *= 1.0 / self.zoomStep
        self.scale(1.0 / self.zoomStep, 1.0 / self.zoomStep)

    def drawBackground(self, painter, rect):
        painter.setBrush(QColor(222, 255, 204))
        painter.drawRect(0, 0, self.conf['x_max'], self.conf['y_max'])
        x0, y0 = self.center().x(), self.center().y()
        painter.drawLine(x0, 0, x0, self.conf['y_max'])
        painter.drawLine(0, y0, self.conf['x_max'], y0)
    
    def center(self):
        return QPoint(self.conf['x_max'] / 2, self.conf['y_max'] / 2)

    def loadSprite(self, filename):
        if self.mainSprite:
            self.scene.removeItem(self.mainSprite)
        pixmap = QPixmap.fromImage(QImage(filename))
        item = QGraphicsPixmapItem(pixmap)
        item.type = 'sprite'
        item.setOffset((self.conf['x_max'] - item.pixmap().width()) / 2,
                       (self.conf['y_max'] - item.pixmap().height()) / 2)
        item.setZValue(-0.1)
        self.mainSprite = item
        self.scene.addItem(item)

    def mousePressEvent(self, mouseEvent):
        if mouseEvent.button() == Qt.LeftButton:
            pos = QPointF(self.mapToScene(mouseEvent.pos()))
            items = self.scene.items(pos)
            if items and items[0].type == 'vertex':
                self.selected = items[0]
                self.grabbed = self.selected
            else:
                if self.mainSprite:
                    point = self.mapToScene(mouseEvent.pos())
                    x = point.x()
                    y = point.y()
                    self.actFixture.addVertex(x, y)
            self.mainWindow.updateText()

    def mouseMoveEvent(self, mouseEvent):
        if self.grabbed:
            point = self.mapToScene(mouseEvent.pos())
            x, y = point.x(), point.y()
            self.moveVertex(self.grabbed, x, y)

    def mouseReleaseEvent(self, mouseEvent):
        self.grabbed = None

    def setMainWindow(self, mainWindow):
        self.mainWindow = mainWindow
    
    def moveVertex(self, vertex, x, y):
        if isinstance(vertex,QGraphicsPixmapItem):
            x -=  vertex.pixmap().width() / 2
            y -=  vertex.pixmap().width() / 2
        if isinstance(vertex, QGraphicsRectItem):
            x -=  vertex.rect().width() / 2
            y -=  vertex.rect().width() / 2
        vertex.setX(x)
        vertex.setY(y)
        self.mainWindow.redrawFixtures()
        self.mainWindow.updateText()

    def moveVertexUp(self):
        if self.selected:
            x, y = self.getPos(self.selected)
            self.moveVertex(self.selected, x, y - 1)

    def moveVertexDown(self):
        if self.selected:
            x, y = self.getPos(self.selected)
            self.moveVertex(self.selected, x, y + 1)        

    def moveVertexLeft(self):
        if self.selected:
            x, y = self.getPos(self.selected)
            self.moveVertex(self.selected, x - 1, y)        
        
    def moveVertexRight(self):
        if self.selected:
            x, y = self.getPos(self.selected)
            self.moveVertex(self.selected, x + 1, y)

    def getPos(self, item):
        if isinstance(item, QGraphicsRectItem):
            x = item.x() + item.rect().width() / 2
            y = item.y() + item.rect().height() / 2
        if isinstance(item, QGraphicsPixmapItem):
            x = item.x() + item.pixmap().width() / 2
            y = item.y() + item.pixmap().height() / 2
        return x, y

    def removeSelectedVertex(self):
        if self.selected:
            self.removeVertex(self.selected)
            if self.actFixture.itemsSorted():
                self.selected = self.actFixture.itemsSorted()[-1]
            else:
                self.selected = None


    def removeVertex(self, vertex):
        self.actFixture.removeVertex(vertex)
        self.actFixture.redrawOutline()
        self.mainWindow.updateText()
        
