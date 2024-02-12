import sys

from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QFileSystemModel,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTreeView,
    QWidget,
)

class BrowserManager():
     
    def __init__(self):
        self._appLayout = None
        self._appWidget = None

    def setup(self):
        self._appLayout = QGridLayout()
        self._appWidget = PresetBrowser(self._appLayout)
        self._appWidget.setResolution(1080, 720)  
        self._appWidget.setup()  


class PresetBrowser(QWidget):

    def __init__(self, layout):
        super().__init__()

        if layout is None:
            raise ValueError("Layout was not created.")

        self._appLayout = layout
        self._appWidth = 250
        self._appHeight = 400
        self._currentDirPath = ''
        self._directoryText = QLineEdit()
        self._sysModel = QFileSystemModel()
        self._treeView = QTreeView()
        self._appTitle = "Preset Browser"
        self._mainLabel = QLabel("Material Library Path")
        self._searchBtn = QPushButton('Search')
        self._findMaterialBtn = QPushButton('Create Material')

    # Public
    def setup(self):
        # Adds widgets to parent layout and set up event callbacks.
        # After setting the correct location in the file system model
        # create the window

        # Add widgets to layout
        self.setLayout(self._appLayout)
        self._appLayout.addWidget(self._mainLabel, 0, 0)
        self._appLayout.addWidget(self._searchBtn, 1, 5, 1, 2)
        self._appLayout.addWidget(self._findMaterialBtn, 6, 0, 1, 7)
        self._appLayout.addWidget(self._treeView, 2, 0, 4, 7)
        self._appLayout.addWidget(self._directoryText, 1, 0, 1, 5)
        
        # setup event callbacks
        self._findMaterialBtn.clicked.connect(self.__importMaterialCallback)
        self._searchBtn.clicked.connect(self.__openBrowserCallback)

        self.__setTreeViewDirectory()
        self.__createWindow()

    def setResolution(self, width, heigth):
        self._appWidth = width
        self._appHeight = heigth

    # Private
    def __setTreeViewDirectory(self, newPath = None):
        # Updates the QTreeView Widget with a new system model that has
        # been set to a new path or the current path avaiable if one has
        # not been provided

        self._currentDirPath = newPath or self._currentDirPath
        self._sysModel.setRootPath(self._currentDirPath)
        self._treeView.setModel(self._sysModel)
        self._treeView.setRootIndex(self._sysModel.index(self._currentDirPath))
        self._directoryText.setText(self._sysModel.rootPath())

    def __createWindow(self):
        self.setGeometry(150, 250,  self._appWidth, self._appHeight)
        self.setWindowTitle(self._appTitle)
        self.show()

    # Event Callbacks
    def __openBrowserCallback(self):
        # Callback to open dialog when _findMaterialBtn is clicked. If a directory
        # is selected it will be use as the new file location for _treeView
        
        newPath = ''
        inputPath = self._directoryText.text()

        # Use what the user has typed in the box
        if inputPath and inputPath != self._currentDirPath:
            newPath = inputPath
        else:
            # Opens a file browser. Only accepts folders as inputs
            newPath = QFileDialog.getExistingDirectory(self, "Select Material Library")

        if newPath:
            self.__setTreeViewDirectory(newPath)
            
    def __importMaterialCallback(self):
        raise NotImplementedError()


# Will run automatically if this file is ran as a script but not if
# the file has been imported as a module.
if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    manager = BrowserManager()
    manager.setup()
    sys.exit(qapp.exec_())
