from pytube import Playlist, YouTube

class DownloadScript:
    def __init__(self):
        self.downloadItems = {}
        self.videos = {}

    def downloadStreams(self):
        print("Preparing to download...")
        path = input("Enter the directory path:")
        for videoID, ITags in self.downloadItems.items():
            yt = self.videos[videoID]
            print("Downloading: " + yt.title)
            for itag in ITags:
                stream = yt.streams.get_by_itag(int(itag))
                filename = [
                    f'Res: {stream.resolution}, FPS: {stream.fps}'
                    f' Video Codec: {stream.video_codec}'
                    f'Audio Codec: {stream.audio_codec}, ABR: {stream.abr}'
                    f'File Type: {stream.mime_type.split("/")[1]}, Size: {stream.filesize // 1024} KB'
                ][0]
                stream.download(path,  yt.title + '__' + filename)
                print("Downloaded", yt.title + '__' + filename)
        print("Downloading complete.")

    def loadStreams(self, url):
        try:
            if url.__contains__('playlist?list'):
                playlist = Playlist(url)
                print("Progress Status: " + playlist.title())
                for video_url in playlist.video_urls:
                    yt = YouTube(video_url)
                    self.videos[yt.video_id] = yt
                    print("Loaded " + yt.title)
            else:
                yt = YouTube(url)
                self.videos[yt.video_id] = yt
                print("Progress Status: " + yt.title)
                print("Loaded: " + yt.title)
        except:
            print("Url doesn't have any video.")
            return False
        print("All Videos are loaded.\n")
        print("Select videos to download.\n\n")
        for videoID, yt in self.videos.items():
            print("\t" + yt.title)
            for stream in yt.streams:
                print(f'ITag: {stream.itag}\n')
                print(f'Res: {stream.resolution}, FPS: {stream.fps}')
                print(f'Video Codec: {stream.video_codec}')
                print(f'Audio Codec: {stream.audio_codec}, ABR: {stream.abr}')
                print(f'File Type: {stream.mime_type.split("/")[1]}, Size: {stream.filesize // 1024} KB\n')
            self.downloadItems[videoID] = input("Enter the ITags of video streams, you wan to download:").replace(' ', '').split(',')
        return True