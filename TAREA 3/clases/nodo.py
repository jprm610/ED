class Nodo:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_left(self):
        return self._left

    def set_left(self, new_left):
        self._left = new_left

    def get_right(self):
        return self._right

    def set_right(self, new_right):
        self._right = new_right
    def __str__(self):
        return f"Nodo con data: {self._data}"
        