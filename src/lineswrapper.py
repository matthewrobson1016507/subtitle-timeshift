# Module to provide very simple friendly API around reading through
# a list of lines read in from a file

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