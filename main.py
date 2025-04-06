import sys
from lineswrapper import LinesWrapper
from subtitle import Subtitle
from subtitleparser import SubtitleParser
from subtitlewriter import SubtitleWriter

def readFile(filepath: str):
    filehandle = open(filepath, 'r', encoding='utf-8-sig')
    contents = list(map(lambda x: x.replace('ueff1', '').replace('\n', '').strip(), filehandle.readlines()))
    filehandle.close()
    return contents

def writeFile(lines: list[str]):
    fileHandle = open('output.srt', 'w')
    fileHandle.writelines(list(map(lambda x: x + '\n', lines)))
    fileHandle.close()

def timeShiftSubtitle(subtitle: Subtitle, nSeconds: int):
    subtitle.timestamp.shiftBy(nSeconds)
    return subtitle

class Args:
    def __init__(self, file: str, nSeconds: int):
        self.file = file
        self.nSeconds = nSeconds

    def parse(argVector: list[str]):
        if len(argVector) != 3:
            return None
        return Args(argVector[1], int(argVector[2]))

def main():
    args = Args.parse(sys.argv)
    if not args:
        print("Wrong number of arguments")
        return
    
    lines = readFile(args.file)
    wrapper = LinesWrapper(lines)
    parser = SubtitleParser()
    subtitleList = parser.parseAllSubtitles(wrapper)

    shiftedSubs = list(map(lambda x: timeShiftSubtitle(x, args.nSeconds), subtitleList ))

    writeFile( SubtitleWriter().writeAllSubtitles(shiftedSubs) )
    
if __name__ == '__main__':
    main()