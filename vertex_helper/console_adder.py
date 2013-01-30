'''
Created on 2011.06.05.

@author: turia
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from spyderlib.widgets.internalshell import InternalShell

def addConsole(root):
    font = QFont("Courier new")
    font.setPointSize(10)
    ns = {'s': root, }
    msg = "self: s"
    # Note: by default, the internal shell is multithreaded which is safer 
    # but not compatible with graphical user interface creation.
    # For example, if you need to plot data with Matplotlib, you will need 
    # to pass the option: multithreaded=False
    root.console = cons = InternalShell(root, namespace=ns, message=msg, multithreaded=False)

    cons.set_font(font)
    cons.set_codecompletion_auto(True)
    cons.set_codecompletion_case(False)
    cons.set_inspector_enabled(True)
    cons.set_calltips(True)
    cons.setup_calltips(size=600, font=font)
    cons.setup_completion(size=(300, 180), font=font)
    console_dock = QDockWidget("Console", root)
    console_dock.setWidget(cons)
    
    # Add the console widget to window as a dockwidget
    root.addDockWidget(Qt.BottomDockWidgetArea, console_dock)
