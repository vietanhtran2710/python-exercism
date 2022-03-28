"""
    Circular buffer exercise
"""
class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class CircularBuffer:
    """
        Class represent a circular buffer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.write_index = 0
        self.read_index = 0
        self.data = [None] * capacity

    def read(self):
        """
            Get the oldest value and remove it
        """
        print(self.data)
        try:
            value = self.data[self.read_index]
            if value is None:
                raise BufferEmptyException("Circular buffer is empty")
            self.data[self.read_index] = None
            self.read_index = (self.read_index + 1) % self.capacity
            return value
        except IndexError:
            raise BufferFullException("Circular buffer is full")

    def write(self, data):
        """
            Write a value into the buffer
        """
        if self.data[self.write_index] is not None:
            raise BufferFullException("Circular buffer is full")
        self.data[self.write_index] = data
        self.write_index = (self.write_index + 1) % self.capacity

    def overwrite(self, data):
        """
            Force write a value into the buffer
        """
        if self.data[self.write_index] is None:
            self.write(data)
        else:
            self.data[self.write_index] = data
            self.read_index = (self.read_index + 1) % self.capacity
            self.write_index = (self.write_index + 1) % self.capacity

    def clear(self):
        """
            Clear the buffer
        """
        self.data = [None] * self.capacity
        self.write_index = 0
        self.read_index = 0
