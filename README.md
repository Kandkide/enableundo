# enableundo
Two classes which have the ability of undo (and redo).

class EnableUndo:
    It has "state" property which can be used to hold variable and object.
    It also has "undo" methods. Ability to undo changes to the State property.

class EnableUndoRedo
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

