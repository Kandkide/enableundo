# coding: utf-8
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
