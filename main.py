import sys
from lineswrapper import LinesWrapper
from subtitleparser import SubtitleParser

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