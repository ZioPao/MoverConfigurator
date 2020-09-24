# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MoverConfiguratorMain(object):
    def setupUi(self, MoverConfiguratorMain):
        MoverConfiguratorMain.setObjectName("MoverConfiguratorMain")
        MoverConfiguratorMain.setEnabled(True)
        MoverConfiguratorMain.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MoverConfiguratorMain.sizePolicy().hasHeightForWidth())
        MoverConfiguratorMain.setSizePolicy(sizePolicy)
        MoverConfiguratorMain.setMinimumSize(QtCore.QSize(500, 300))
        MoverConfiguratorMain.setMaximumSize(QtCore.QSize(500, 300))
        MoverConfiguratorMain.setAnimated(True)
        MoverConfiguratorMain.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MoverConfiguratorMain)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 250, 121, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.findFolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.findFolderButton.setEnabled(True)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 80, 271, 71))
        self.textEdit.setObjectName("textEdit")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findFolderButton.sizePolicy().hasHeightForWidth())
        self.findFolderButton.setSizePolicy(sizePolicy)
        self.findFolderButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.findFolderButton.setBaseSize(QtCore.QSize(30, 30))
        self.findFolderButton.setMouseTracking(False)
        self.findFolderButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.findFolderButton.setObjectName("findFolderButton")
        self.findFolderButton.clicked.connect(SearchFolder)
        self.verticalLayout.addWidget(self.findFolderButton)
        MoverConfiguratorMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MoverConfiguratorMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        self.menubar.setObjectName("menubar")
        MoverConfiguratorMain.setMenuBar(self.menubar)

        self.retranslateUi(MoverConfiguratorMain)
        QtCore.QMetaObject.connectSlotsByName(MoverConfiguratorMain)

    def retranslateUi(self, MoverConfiguratorMain):
        _translate = QtCore.QCoreApplication.translate
        MoverConfiguratorMain.setWindowTitle(_translate("MoverConfiguratorMain", "MoverConfigurator"))
        self.findFolderButton.setText(_translate("MoverConfiguratorMain", "Cerca cartella"))

    def setFolder(self, folder):
        self.textEdit.setText(folder)


class SearchFolder(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Seleziona la cartella")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openFolderDialog()


        self.show()

    def openFolderDialog(self):
        folderDialog = QtWidgets.QFileDialog
        folder = folderDialog.getExistingDirectory(self, "Seleziona la cartella", "",
                                                               QtWidgets.QFileDialog.ShowDirsOnly or QtWidgets.QFileDialog.DontResolveSymlinks)
        if folder:
            ui.setFolder(folder)
            print(folder)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MoverConfiguratorMain()
    ui.setupUi(window)
    window.show()

    sys.exit(app.exec_())
