# coding: utf-8
import pickle
import copy


class EnableUndo:
    """It has "state" property which can be used to hold variable and object.
    It also has "undo" methods. Ability to undo changes to the State property.
    """
    def __init__(self) -> None:
        self._mementos = []
        self._state = None
    
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if self._state != value:
            self._backup()
            self._state = value

    def _backup(self) -> object:
        self._mementos.append(pickle.dumps(vars(self)))
        return self

    def undo(self) -> bool:
        if len(self._mementos) > 0:
            vars(self).update(pickle.loads(self._mementos.pop()))
            return True
        else:
            # print('Cannot undo. There is no backup.')
            return False


class EnableUndoRedo:
    """It has "state" property which can be used to hold variable and object.
    It also has "undo" and "redo"  methods, 
    which are the ability to redo or undo changes to the State property.
    """
    def __init__(self) -> None:
        self._mementos = []
        self._backward_mementos = []
        self._state = None
    
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if self._state != value:
            self._backup()
            self._state = value

    def _backup(self, reset_backward=True) -> object:
        self._mementos.append(pickle.dumps(vars(self)))
        if reset_backward is True:
            self._backward_mementos = []
        return self._mementos

    def _backward_backup(self) -> object:
        self._backward_mementos.append(pickle.dumps(vars(self)))
        return self._backward_mementos

    def undo(self) -> bool:
        if len(self._mementos) > 0:
            copied = copy.deepcopy(self._backward_backup())
            vars(self).update(pickle.loads(self._mementos.pop()))
            self._backward_mementos = copied
            return True
        else:
            # print('Cannot undo. There is no backup.')
            return False

    def redo(self) -> bool:
        if len(self._backward_mementos) > 0:
            copied = copy.deepcopy(self._backup(reset_backward=False))
            vars(self).update(pickle.loads(self._backward_mementos.pop()))
            self._mementos = copied
            return True
        else:
            # print('Cannot redo. There is no backward_backup.')
            return False



# [Reference] https://note.com/fz5050/n/n62bca270145f