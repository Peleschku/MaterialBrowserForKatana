import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import (QFont,
                         QFontDatabase)


class PresetBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.createWindow()

    
    def createWindow(self):

        appWidth = 600
        appHeight = 800

        self.setGeometry(150, 250, appWidth, appHeight)
        self.setWindowTitle('Preset Browser')
        self.populateUI()
        self.setLayout(self.layout)
        self.show()

    def populateUI(self):


        # setting up search field
        setDirectory = QLabel('Material library Path')
        self.storeDirectory = QLineEdit()
        self.search = QPushButton('Search')

        self.search.clicked.connect(self.openBrowser)

        self.layout.addWidget(setDirectory, 0, 0)
        self.layout.addWidget(self.storeDirectory, 1, 0, 1, 5)
        self.layout.addWidget(self.search, 1, 5, 1, 2)

        # Tree view of folder location specified above
        # TODO: figure out why the model isn't looking at the file path
        # that is added to the QLineEdit after a folder is specified

        self.dirPath = ''
        self.model = QFileSystemModel()
        self.model.setRootPath(self.dirPath)

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.dirPath))

        self.layout.addWidget(self.tree, 2, 0, 4, 7)

        self.createMaterial = QPushButton('Search')
        self.createMaterial.clicked.connect(self.importMaterial)

        self.layout.addWidget(self.createMaterial, 6, 0, 1, 7)
                         

        self.show()
    
    def openBrowser(self):
        
        # opens a file browser. Only accepts folders as inputs
        filePath = QFileDialog.getExistingDirectory(self, "Select Material Library")

        # adds the selected folder to the QLineEdit
        if filePath:
            self.storeDirectory.insert(filePath)
            self.populateUI()
            self.dirPath = filePath
    
    def importMaterial(self):
        print(self.dirPath)


app = QApplication(sys.argv)
myWindow = PresetBrowser()
sys.exit(app.exec())
