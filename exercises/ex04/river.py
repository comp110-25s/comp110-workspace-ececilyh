"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    day: int
    bears: list[str]
    fish: list[str]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        age = age
        fish_idx = 0
        bear_idx = 0
        fish_new: list []
        bear_new: list []
        while fish_idx >= len (self.fish):
            if self.fish(age) <= 3:
                fish_new.append (fish_idx)
            fish_idx += 1
        while bear_idx >= len (self.bear):
            if self.bear (age) <= 5:
                bear_new.append (fish_idx)
            bear_idx += 1
        self.bears = bear_new
        self.fish = fish_new
        return None
    
    def remove_fish (self, amount: int) -> None:
        amount = 0
        self.fish.pop (len(amount))


    def bears_eating(self):
        if num_fish >= 5:
            remove_fish(amount = 3)
            eat (num_fish)
        return None

    def check_hunger(self):
       idx = 0
       bear_new = self.bears
       while idx <= len(bears):
           if hunger_score < 0:
               bear_new.pop (idx)
        self.bears = bear_new
        return None

    def repopulate_fish(self):
        n = [(num_fish//2)*4]
        self.fish.append (n)
        return None

    def repopulate_bears(self):
        return None

    def view_river(self) -> None:
        day = day
        num_fish = len(fish)
        num_bear = len(bears)
        print(f"~~~ Day {day}: ~~~")
        print(f"Fish population: {num_fish}")
        print(f"Bear population: {num_bear}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
    
    def one_river_week (self) -> None:
        print one_river_day ()
        print one_river_day ()
        print one_river_day ()
        print one_river_day ()
        print one_river_day ()
        print one_river_day ()
        print one_river_day ()