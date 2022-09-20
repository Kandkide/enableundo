# coding: utf-8
# Allow importing modules from the perspective of one directory above.
if __name__ == '__main__':
    import os, sys; sys.path.append(os.path.join(os.path.dirname(__file__), '..' ))
    
from enableundo import EnableUndoRedo

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
