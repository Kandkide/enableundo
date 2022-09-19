# coding: utf-8
from undoredo import EnableUndoRedo


class Tokyo(EnableUndoRedo):
    def __init__(self) -> None:
        super().__init__()
        self.weather = 'sunny'
        self.hour = 0
    
    def timepassed(self):
        self.hour += 1
        self.hour = self.hour % 24
        self.weather = ['cloudy', 'rainy', 'sunny', 'snow', 'stormy'][self.hour % 5]
        self.show()

    def show(self):
        print(f"{self.hour}:00 {self.weather}")

def main():
    tokyo = Tokyo()
    tokyo.show()

    for i in range(23):
        if i % 6 == 0:
            tokyo.state = i
        tokyo.timepassed()

    print()

    for i in range(4):
        tokyo.undo()
        tokyo.show()

main()