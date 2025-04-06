import sys
from lineswrapper import LinesWrapper
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

def main():
    subtitleFilePath = sys.argv[1]
    lines = readFile(subtitleFilePath)
    wrapper = LinesWrapper(lines)
    parser = SubtitleParser()
    subtitleList = parser.parseAllSubtitles(wrapper)
    writeFile( SubtitleWriter().writeAllSubtitles(subtitleList) )
    
if __name__ == '__main__':
    main()