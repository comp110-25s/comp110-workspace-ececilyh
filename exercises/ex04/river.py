"""File to define River class."""

___author___: "730551362"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Creating the River class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of fish and bears."""
        fish_idx = 0
        bear_idx = 0
        fish_new: list[Fish] = []
        bear_new: list[Bear] = []
        while fish_idx < len(self.fish):
            if self.fish[fish_idx].age <= 3:
                fish_new.append(self.fish[fish_idx])
            fish_idx += 1
        while bear_idx < len(self.bears):
            if self.bears[bear_idx].age <= 5:
                bear_new.append(self.bears[bear_idx])
            bear_idx += 1
        self.bears = bear_new
        self.fish = fish_new
        return None

    def remove_fish(self, amount: int) -> None:
        """Removing fish when they are eaten."""
        i: int = 0
        while i < amount:
            self.fish.pop(0)
            i += 1

    # Need to call it on self because self IS a River...
    # this means it applies to the entire group.
    # Class has a capital.

    def bears_eating(self):
        """Feeding bears."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(amount=3)
                bear.eat(num_fish=3)
        return None

    # Creating new list, going through old list for the surviving list,
    # then replacing.
    # If accessing attribute, just put the dot and name.
    # Variable (that rep object).method
    def check_hunger(
        self,
    ):
        """Checking the hunger scores of each bear."""
        bear_new: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bear_new.append(bear)
        self.bears = bear_new
        return None

    def repopulate_fish(self):
        """Modeling the river's fish population."""
        num_fish = len(self.fish)
        n = (num_fish // 2) * 4
        i = 0
        while i < n:
            self.fish.append(Fish())
            i += 1
        return None

    def repopulate_bears(self):
        """Modeling the river's bear population."""
        num_bear = len(self.bears)
        n = num_bear // 2
        i = 0
        while i < n:
            self.bears.append(Bear())
            i += 1
        return None

    def view_river(self) -> None:
        """Checking the fish and bear populations on a given day."""
        num_fish = len(self.fish)
        num_bear = len(self.bears)
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {num_fish}")
        print(f"Bear population: {num_bear}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Calling a week-worth of days in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
