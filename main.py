import sys

class LinesWrapper:
    def __init__ (self, lines: list[int]):
        self.lines = lines
        self.currentIndex = 0

    def readNext(self):
        if self.atEnd():
            return None

        next = self.lines[self.currentIndex]
        self.currentIndex = self.currentIndex + 1
        return next
    
    def atEnd(self):
        return self.currentIndex == len(self.lines) - 1
    
    def goBackOnePlace(self):
        if self.currentIndex > 0:
            self.currentIndex = self.currentIndex - 1

class SubtitleTimeStamp:
    def __init__(self, startTime: str, endTime: str):
        self.startTime = startTime
        self.endTime = endTime

class Subtitle:
    def __init__(self, index: int, timestamp: SubtitleTimeStamp, subtitleContents: list[str]):
        self.index = index
        self.timestamp = timestamp
        self.subtitleContents = subtitleContents

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

def readFile(filepath: str):
    filehandle = open(filepath, 'r', encoding='utf-8-sig')
    contents = list(map(lambda x: x.replace('ueff1', '').replace('\\n', '').strip(), filehandle.readlines()))
    filehandle.close()
    return contents

def main():
    subtitleFilePath = sys.argv[1]
    lines = readFile(subtitleFilePath)
    wrapper = LinesWrapper(lines)
    parser = SubtitleParser()
    subtitleList = parser.parseAllSubtitles(wrapper)

if __name__ == '__main__':
    main()