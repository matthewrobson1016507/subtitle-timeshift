# Subtitle Timeshift Utility

Command line tool written in python to take a .srt subtitle file and shift the timestamps of all the subtitles either earlier or later in time by a specified number of seconds.

This came about when I downloaded a subtitle file from [this repository of Japanese subtitles](https://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F), (which I found on [AwesomeJapanese](https://github.com/yudataguy/Awesome-Japanese)), I found that for the particular show I'd picked the subtitles were offset compared to the audio on my video file. 

So I wrote a python program to parse the .srt file and output a new .srt file with the timestamps shifted, so that I could make my subtitles be in sync.

## Usage
```shell
subtitle-timeshift <path-to-srt-file> <time-shift>
```
The amount to shift the timestamps of the subtitles by is given as a parameter which represents the amount of time to shift the subtitles by in seconds.

* To shift the subtitles to be LATER, pass a POSITIVE number
* To shift the subtitles to be EARLIER, pass a NEGATIVE number

The new .srt file with the shifted subtitles is created as a file called `output.srt` in the current working directory.