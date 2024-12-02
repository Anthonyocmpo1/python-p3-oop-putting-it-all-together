class Shoe:
    def __init__(self, brand, size):
        """
        Initialize a Shoe instance with a brand and size.
        """
        self.brand = brand
        self._size = None  # Use a private attribute for validation
        self.size = size  # Trigger the setter for initial validation
        self.condition = "New"  # Default condition is "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        """
        Repairs the shoe and sets its condition to 'New'.
        """
        self.condition = "New"
        print("Your shoe is as good as new!")
