# Module to represent parsing subtitle entries form an srt file

from datetime import timedelta

def __div_int_part__(num: int, denom: int):
    return divmod(num, denom)[0]

def __two_digit_string__(value: int):
    if value < 10:
        return '0' + str(value)
    else:
        return str(value)
    
def __three_digit_string__(value: int):
    if value < 10:
        return '00' + str(value)
    elif value < 100:
        return '0' + str(value)
    else:
        return str(value)

class SubtitleTimeStamp:
    def __init__(self, startTime: str, endTime: str):
        self.startTime = startTime
        self.endTime = endTime

    # Shift the timestamp of the subtitle by a time-shift given in seconds
    # Pass in a POSITIVE number to shift the timestamp to be LATER
    # Pass in a NEGATIVE number to shift the timestamp to be EARLIER
    def shiftBy(self, nSeconds):
        convertedStart = self.__convert_from_string__(self.startTime)
        convertedEnd = self.__convert_from_string__(self.endTime)
        newStart = convertedStart + timedelta(seconds=nSeconds)
        newEnd = convertedEnd + timedelta(seconds=nSeconds)
        self.startTime = self.__convert_back_to_string__(newStart)
        self.endTime = self.__convert_back_to_string__(newEnd)

    def __convert_from_string__(self, s: str):
        hourMinuteSecondStr, microSecondStr = s.split(',')
        hourStr, minuteStr, secondStr = hourMinuteSecondStr.split(':')
        return timedelta(
            hours=int(hourStr),
            minutes=int(minuteStr),
            seconds=int(secondStr),
            microseconds=int(microSecondStr) * 1000
        )

    def __convert_back_to_string__(self, t: timedelta):
        totalSeconds = t.seconds
        hours = __div_int_part__(totalSeconds, 3600)
        minutes = __div_int_part__(totalSeconds - hours * 3600, 60)
        seconds = ( totalSeconds - hours * 3600 - minutes * 60 )
        hourMinuteSecondStr = str.join(':', map(lambda x: __two_digit_string__(x), [hours, minutes, seconds]))
        millisecondStr = __three_digit_string__( __div_int_part__(t.microseconds,1000) )
        return str.join( ',', [hourMinuteSecondStr, millisecondStr] )


class Subtitle:
    def __init__(self, index: int, timestamp: SubtitleTimeStamp, subtitleContents: list[str]):
        self.index = index
        self.timestamp = timestamp
        self.subtitleContents = subtitleContents

