# enableundo
Two classes which have the ability of undo (and redo).

class EnableUndo:

    It has "state" property which can be used to hold variable and object.
    It also has "undo" methods. Ability to undo changes to the State property.

class EnableUndoRedo:

    It has "redo" method in addition.

# Usage
1, Make an instance

    tokyo = EnableUndoRedo()

2, Set some value to 'state' property.

    tokyo.state = 'coudy morning'
    tokyo.state = 'sunny noon'
    tokyo.state = 'rainy night'

3, Use undo (and redo) method.

    tokyo.undo()

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

# Application

    In fact, the instance itself is undoable, not just the 'state' property. Therefore, if you derive a subclass and add any property, the added property can also be involved in undo and redo. The state is saved when a new value is assigned to the state property. Therefore, by using the state property like a timekeeper, you can control when the state is saved.



