from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
from pytube import Playlist, YouTube

from Structure.StreamTreeItem import StreamTreeItem


class Streams(QObject):
    signalError = pyqtSignal(str)
    signalMessage = pyqtSignal(str)
    signalProgress = pyqtSignal(int)
    signalStatus = pyqtSignal(str)
    signalWorkDone = pyqtSignal(bool)

    def __init__(self, window, parent=None):
        super(Streams, self).__init__(parent=None)
        self.videos = {}
        self.window = window

        self.signalError.connect(self.window.showError)
        self.signalMessage.connect(self.window.messageL.setText)
        self.signalProgress.connect(self.window.progressPB.setValue)
        self.signalStatus.connect(self.window.statusL.setText)
        self.signalWorkDone.connect(self.window.loadWidget)
    
    def downloadStreams(self):
        IDS = self.window.checkItems()
        path = self.window.directoryL.text()
        for videoID, ITag, filename in IDS:
            yt = self.videos[videoID]
            self.signalMessage.emit("Dowloading: " + yt.title)
            self.signalProgress.emit(0)
            yt.register_on_progress_callback(self.notify)
            stream = yt.streams.get_by_itag(ITag)
            stream.download(path,  yt.title + '__' + filename)
    
    def loadStreams(self):
        url = self.window.urlLE.text()
        try:
            if url.__contains__('playlist?list'):
                playlist = Playlist(url)
                self.signalStatus.emit("Progress Status: " + playlist.title())
                index, total = 0, len(playlist.video_urls) * 2
                for video_url in playlist.video_urls:
                    yt = YouTube(video_url)
                    self.videos[yt.video_id] = yt
                    self.signalMessage.emit("Loaded " + yt.title)
                    self.signalProgress.emit(int((index + 1) / total * 100))
                    index += 1
            else:
                yt = YouTube(url)
                self.videos[yt.video_id] = yt
                self.signalStatus.emit("Progress Status: " + yt.title)
                self.signalMessage.emit("Loaded: " + yt.title)
        except:
            self.signalError.emit("Url doesn't have any video.")
            return None
        self.signalProgress.emit(50)
        for videoID, yt in self.videos.items():
            streamHead = StreamTreeItem([yt.title], videoID, parent=self.window.streamsTW)
            audioHead = StreamTreeItem(['Audio Only'], videoID)
            index, total = 0, len(list(self.videos.keys())) * len(yt.streams)
            for stream in yt.streams:
                if stream.video_codec is None:
                    title = [
                        f'Codec: {stream.audio_codec}, '
                        f'ABR: {stream.abr}, '
                        f'File Type: {stream.mime_type.split("/")[1]}, '
                        f'Size: {stream.filesize // 1024} KB'
                    ]
                    audioHead.addChild(StreamTreeItem(title, videoID, stream.itag))
                else:
                    title = [
                        f'Res: {stream.resolution}, FPS: {stream.fps}, '
                        f' Video Codec: {stream.video_codec}, Audio Codec: {stream.audio_codec}, '
                        f'File Type: {stream.mime_type.split("/")[1]}, '
                        f'Size: {stream.filesize // 1024} KB'
                    ]
                    streamHead.addChild(StreamTreeItem(title, videoID, stream.itag))
                index += 1
                self.signalProgress.emit(int(50 + index / total * 100))
            streamHead.addChild(audioHead)
        self.signalProgress.emit(100)
        self.signalWorkDone.emit(True)
    
    def notify(self, stream, chunk, bytes_remaining):
        file_size = stream.filesize
        self.signalProgress.emit(int((file_size - bytes_remaining) / file_size * 100))
