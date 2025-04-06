# Module to encapsulate writing a list of subtitles to file

from subtitle import Subtitle, SubtitleTimeStamp

class SubtitleWriter:
    def writeAllSubtitles(self, subtitles: list[Subtitle]):
        lines = list[str]()
        for sub in subtitles:
            for subtitleLine in self.writeOneSubtitle(sub):
                lines.append(subtitleLine)
        return lines
    
    def writeOneSubtitle(self, subtitle: Subtitle):
        lines = list[str]()
        lines.append(str(subtitle.index))
        lines.append(self.__write_timestamp_string__(subtitle.timestamp))
        for line in subtitle.subtitleContents:
            lines.append(line)
        return lines
    
    def __write_timestamp_string__(self, timestamp: SubtitleTimeStamp):
        return str.join(' ', [timestamp.startTime, '-->', timestamp.endTime])