"""File to define Bear class."""

___author___ = "730551362"


class Bear:
    """Creating the Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing the ages and hunger scores of the Bear class."""
        self.age: int = 0
        self.hunger_score: int = 0

    def one_day(self) -> None:
        """Modeling one day in a bear's life on the river."""
        self.hunger_score -= 1
        self.age += 1

    def eat(self, num_fish: int) -> None:
        """Defining what happens when the bear eats."""
        self.hunger_score += num_fish
