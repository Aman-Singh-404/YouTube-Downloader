import requests
from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from Interface.UI_Downloader import Ui_MainWindow
from Structure.Streams import Streams
from Structure.StreamTreeItem import StreamTreeItem


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.threads = []
        self.thumbnail_ID = None
        self.stream = None

        self.directoryL.mouseDoubleClickEvent = self.browse
        
        self.cancelPB.clicked.connect(self.close)
        self.downloadPB.clicked.connect(self.downloadStreams)
        self.loadurlPB.clicked.connect(self.loadStreams)
        self.streamsTW.itemClicked.connect(self.setThumbnail)
    
    def browse(self, event):
        path = self.directoryL.text()
        path = QFileDialog.getExistingDirectory(self, "Select Directory", path)
        if path != "":
            self.directoryL.setText(path)
    
    def checkItems(self):
        IDS = []
        for index in range(self.streamsTW.topLevelItemCount()):
            head = self.streamsTW.topLevelItem(index)
            for i in range(head.childCount()):
                child = head.child(i)
                if child.ITag != None and child.checkState(0):
                    IDS.append((child.videoID, child.ITag, child.text(0)))
        return IDS

    def downloadStreams(self):
        if self.checkItems() == []:
            QMessageBox.warning(self, "Alert", "Nothing is selected.")
        elif self.directoryL.text() == '':
            QMessageBox.warning(self, "Alert", "Download path not selected.")
        else:
            self.messageL.setText('')
            self.statusL.setText('Progress Status:')
            self.progressPB.setValue(0)

            thread = QThread()
            self.threads.append(thread)
            thread.started.connect(self.stream.downloadStreams)
            thread.start()
    
    def initStreams(self):
        self.thumbnail_ID = None
        self.thumbnailL.setText("Thumbnail Preview")
        self.streamsTW.clear()
        for thread in self.threads:
            thread.quit()
            thread.wait()
        if self.stream != None:
            self.stream.deleteLater()
        self.stream = None
        self.threads.clear()
        self.thumbnail_ID = None
        self.thumbnailL.setText("Thumbnail Preview")
        self.streamsTW.clear()
    
    def loadWidget(self, value):
        self.cancelPB.setEnabled(value)
        self.directoryL.setEnabled(value)
        self.downloadPB.setEnabled(value)
        self.label_3.setEnabled(value)
        self.loadurlPB.setEnabled(value)
        self.streamsTW.setEnabled(value)
        self.urlLE.setEnabled(value)
        if not value:
            self.messageL.setText('')
            self.statusL.setText('Progress Status:')
            self.progressPB.setValue(0)
    
    def loadStreams(self):
        if self.urlLE.text().strip() == '':
            QMessageBox.warning(self, "Alert", "URL can't be empty.")
            return None
        self.initStreams()
        self.stream = Streams(self)
        thread = QThread()
        self.threads.append(thread)
        self.stream.moveToThread(thread)
        
        self.loadWidget(False)
        
        thread.started.connect(self.stream.loadStreams)
        thread.start()
    
    def setThumbnail(self, item, column):
        if self.thumbnail_ID == item.videoID:
            return None
        thumbnail = QPixmap()
        thumbnail_url = self.stream.videos[item.videoID].thumbnail_url
        thumbnail_url = f'{thumbnail_url.rsplit("/", 1)[0]}/mqdefault.jpg'
        
        req = requests.get(thumbnail_url, stream = True)
        thumbnail.loadFromData(req.content)
        self.thumbnailL.setPixmap(thumbnail)
        self.thumbnailL.setScaledContents(True)
        self.thumbnail_ID = item.videoID
    
    def showError(self, err_msg):
        QMessageBox.warning(self, "Alert", err_msg)
        
        self.cancelPB.setEnabled(True)
        self.loadurlPB.setEnabled(True)
        self.streamsTW.setEnabled(True)
        self.urlLE.setEnabled(True)
        self.messageL.setText('')
        self.statusL.setText('Progress Status:')
        self.progressPB.setValue(0)
