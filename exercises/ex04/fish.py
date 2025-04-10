"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        """Initalizing the age of a fish."""
        self.age: int = 0

    def one_day(self) -> None:
        """Modeling one day in a fish's life on the river."""
        self.age += 1
