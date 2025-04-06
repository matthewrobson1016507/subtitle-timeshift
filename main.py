from lineswrapper import LinesWrapper
from subtitle import Subtitle
from subtitleparser import SubtitleParser
from subtitlewriter import SubtitleWriter
from argparse import ArgumentParser

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

parser = ArgumentParser(
    prog='subtitle-timeshift',
    description='Command line tool to shift timestamps of the subtitles in a subtitle file by a fixed time shift'
)

parser.add_argument(
    'subtitleFile', 
    help='Path to the subtitle file to be read',
    type=str
)

parser.add_argument(
    'nSeconds', 
    help='The number of seconds to shift the subtitle timestamps by, enter a negative value to shift them earlier',
    type=int
)

def main(args):    
    lines = readFile(args.subtitleFile)
    wrapper = LinesWrapper(lines)
    parser = SubtitleParser()
    subtitleList = parser.parseAllSubtitles(wrapper)

    shiftedSubs = list(map(lambda x: timeShiftSubtitle(x, args.nSeconds), subtitleList ))

    writeFile( SubtitleWriter().writeAllSubtitles(shiftedSubs) )
    
if __name__ == '__main__':
    main( parser.parse_args() )