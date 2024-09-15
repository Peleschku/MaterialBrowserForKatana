import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MaterialExporterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.createWindow()

    def createWindow(self):
        self.setGeometry(250, 250, 500, 250)
        self.setWindowTitle('UI Test')

        self.populateUI()
        self.show()
    
    def populateUI(self):
        layout = QGridLayout()
        
        # export path setup
        exportPathLabel = QLabel('exportLocation')
        self.exportBrowser = QLineEdit()

        self.searchButton = QPushButton('Search')
        self.searchButton.clicked.connect(self.exportBrowserPopUp)

        layout.addWidget(exportPathLabel, 0,0)
        layout.addWidget(self.exportBrowser, 0,1)
        layout.addWidget(self.searchButton, 0,2)

        # export type setup
        exportTypeLabel = QLabel('exportType')
        self.typeDropdown = QComboBox()

        fileTypes = ['.klf', '.usd', '.usda', '.usdz']

        for i in fileTypes:
            self.typeDropdown.addItem(i)
        
        layout.addWidget(exportTypeLabel, 1, 0)
        layout.addWidget(self.typeDropdown, 1, 1)

        # render button
        self.exportMaterialBttn = QPushButton('Export Material')
        self.exportMaterialBttn.clicked.connect(self.exportMaterial)

        layout.addWidget(self.exportMaterialBttn, 2,1)

        self.show()
        self.setLayout(layout)

    def exportBrowserPopUp(self):
        self.filePath = QFileDialog.getOpenFileName(self, 'select folder', "", "")

        if self.filePath:
            self.exportBrowser.insert(self.filePath[0])

    def exportMaterial(self):
        print(f"Saving material to {self.filePath}")
        dropDownText = self.typeDropdown.currentText()
        print(f"Exporting {dropDownText} material")


app = QApplication(sys.argv)
myWindow = MaterialExporterUI()
sys.exit(app.exec_())




