import sys

from PyQt5.QtWidgets import QApplication

from Structure.CLI_Script import DownloadScript
from Structure.Window import Window

if __name__ == "__main__":
    if len(sys.argv) == 1:
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())
    else:
        print("\t\tYouTube downloader\n\n")
        ds = DownloadScript()
        if ds.loadStreams(sys.argv[1]):
            ds.downloadStreams()
