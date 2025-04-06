# Module to represent parsing subtitle entries form an srt file

class SubtitleTimeStamp:
    def __init__(self, startTime: str, endTime: str):
        self.startTime = startTime
        self.endTime = endTime

class Subtitle:
    def __init__(self, index: int, timestamp: SubtitleTimeStamp, subtitleContents: list[str]):
        self.index = index
        self.timestamp = timestamp
        self.subtitleContents = subtitleContents

