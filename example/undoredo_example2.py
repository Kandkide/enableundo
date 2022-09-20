# coding: utf-8
# Allow importing modules from the perspective of one directory above.
if __name__ == '__main__':
    import os, sys; sys.path.append(os.path.join(os.path.dirname(__file__), '..' ))
    
from enableundo import EnableUndoRedo

# Class Tokyo derives from EnableUndoRedo with some additional properties (weather and hour).
class Tokyo(EnableUndoRedo):
    def __init__(self) -> None:
        super().__init__()
        self.weather = 'sunny'
        self.hour = 0
    
    # Advance time by 1 hour (Increase self.hour by 1)
    def timepassed(self):
        self.hour += 1
        self.hour = self.hour % 24
        # Change the weather attribute (although it just cycles)
        self.weather = ['cloudy', 'rainy', 'sunny', 'snow', 'stormy'][self.hour % 5]
        self.show()

    def show(self):
        print(f"{self.hour}:00 {self.weather}")


tokyo = Tokyo()
tokyo.show()

for i in range(23):
    if i % 6 == 0:
        # Every 6 hours the 'state' property is updated. 
        # At this time, the entire instance (tokyo) is snapshotted.
        tokyo.state = i
    tokyo.timepassed()

print()

for i in range(4):
    # Each time you undo, roll back the attributes of the tokyo object 
    # for 6 hours (that is, at each snapshot timing).
    tokyo.undo()
    tokyo.show()
