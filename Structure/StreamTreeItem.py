from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem


class StreamTreeItem(QTreeWidgetItem):
    def __init__(self, title, videoID, ITag=None, parent=None):
        super(StreamTreeItem, self).__init__(parent, title)
        self.videoID = videoID
        self.ITag = ITag
        
        if ITag != None:
            self.setCheckState(0, Qt.Unchecked)
