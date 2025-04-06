from lineswrapper import LinesWrapper
from subtitle import Subtitle, SubtitleTimeStamp

class SubtitleParser:
    # Parses all subtitles in the lines provided and compiles them
    # in a list of parsed subtitle objects;
    # stops if a parsing error is encountered
    def parseAllSubtitles(self, linesWrapper: LinesWrapper):
        keepParsing = True
        subtitles = list[Subtitle]()
        while keepParsing:
            nextSub = self.parseOneSubtitle(linesWrapper)
            if not nextSub:
                keepParsing = False
            else:
                subtitles.append(nextSub)
        return subtitles

    # Parses a single subtitle entry 
    # and creates a corresponding subtitle object
    # Returns the parsed subtitle object or None if the parsing fails
    def parseOneSubtitle(self, linesWrapper: LinesWrapper):
        indexLine = self.__get_next_line__(linesWrapper)

        if not indexLine.isdigit():
            return None
        index = int(indexLine)

        timeStampLine = self.__get_next_line__(linesWrapper)
        timeStampParts = timeStampLine.split('-->')
        if len(timeStampParts) != 2:
            return None
        timestamp = SubtitleTimeStamp(timeStampParts[0], timeStampParts[1])

        nextLine = self.__get_next_line__(linesWrapper)
        subtitleContents = list[str]()
        while not linesWrapper.atEnd() and not nextLine.isdigit():
            subtitleContents.append(nextLine)
            nextLine = self.__get_next_line__(linesWrapper)
        
        if nextLine.isdigit():
            linesWrapper.goBackOnePlace()

        return Subtitle(index, timestamp, subtitleContents)

    def __get_next_line__(self, linesWrapper: LinesWrapper):
        line = ''
        while line == '' and not linesWrapper.atEnd():
            line = linesWrapper.readNext()
        return line