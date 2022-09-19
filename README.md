# enableundo
Two classes which have the ability of undo (and redo).

class EnableUndo:

    It has "state" property which can be used to hold variable or object.
    It also has "undo" methods. Ability to undo changes to the State property.

class EnableUndoRedo:

    It has "redo" method in addition to the above.

# Usage
1, Make an instance

    tokyo = EnableUndoRedo()

2, Set some value to 'state' property.

    tokyo.state = 'coudy morning'
    tokyo.state = 'sunny noon'
    tokyo.state = 'rainy night'

3, Use undo (and redo) method.

    tokyo.undo()
    tokyo.redo()

# Example 1

    from undoredo import EnableUndoRedo

    tokyo = EnableUndoRedo()

    tokyo.state = 'coudy morning'
    tokyo.state = 'sunny noon'
    tokyo.state = 'rainy night'

    print(tokyo.state)
    tokyo.undo()
    print(tokyo.state)
    tokyo.undo()
    print(tokyo.state)
    tokyo.undo()
    print(tokyo.state)

    print()

    tokyo.redo()
    print(tokyo.state)
    tokyo.redo()
    print(tokyo.state)
    tokyo.redo()
    print(tokyo.state)


Result:

    rainy night
    sunny noon
    coudy morning
    None

    coudy morning
    sunny noon
    rainy night

# Application

In fact, the instance itself is undo-able, not just the 'state' property. Therefore, if you derive a subclass and add any property, the added property can also be involved in undo and redo. A snapshot of the instance is saved when a new value is assigned to the 'state' property. So you can control the timing of snapshots by using the 'state' property like a timekeeper.

See next example 2.

# Example 2

## Snapshots and rollbacks of class instances

    from undoredo import EnableUndoRedo

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


Result:

    0:00 sunny
    1:00 rainy
    2:00 sunny
    3:00 snow
    4:00 stormy
    5:00 cloudy
    6:00 rainy
    7:00 sunny
    8:00 snow
    9:00 stormy
    10:00 cloudy
    11:00 rainy
    12:00 sunny
    13:00 snow
    14:00 stormy
    15:00 cloudy
    16:00 rainy
    17:00 sunny
    18:00 snow
    19:00 stormy
    20:00 cloudy
    21:00 rainy
    22:00 sunny
    23:00 snow

    18:00 snow
    12:00 sunny
    6:00 rainy
    0:00 sunny
