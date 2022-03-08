"""
    React exercise
"""

class InputCell:
    """
        Cell with initialize value
    """
    def __init__(self, initial_value):
        self._value = initial_value
        self.parent = []

    @property
    def value(self):
        """
            Return its own value
        """
        return self._value

    @value.setter
    def value(self, __value):
        self._value = __value
        for parent in self.parent:
            parent.check_from_children()


class ComputeCell:
    """
        Cell with value computed from other cells
    """
    def __init__(self, inputs, compute_function):
        self._value = compute_function([inp.value for inp in inputs])
        self.inputs = inputs
        self.function = compute_function
        self.parent = []
        self.callbacks = []
        for cell in inputs:
            cell.parent.append(self)

    @property
    def value(self):
        """
            Calculate value from its inputs and call callbacks if value changed
        """
        return self.function([inp.value for inp in self.inputs])

    @value.setter
    def value(self, __value):
        self._value = __value

    def check_from_children(self):
        """
            Update value when children value is changed
        """
        result = self.function([inp.value for inp in self.inputs])
        if result != self._value:
            for callback in self.callbacks:
                callback(result)
            self._value = result
            for parent in self.parent:
                parent.check_from_children()

    def add_callback(self, callback):
        """
            Add value updated function callback
        """
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        """
            Remove value updated function callback
        """
        try:
            self.callbacks.remove(callback)
        except ValueError:
            pass
