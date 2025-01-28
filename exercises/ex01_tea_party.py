"""Planning for a tea party!"""

__author__: str = "730551362"


def main_planner(guests: int) -> None:
    """An entry function."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    return None


def tea_bags(people: int) -> int:
    """A function for tea drinkers."""
    return 2 * people


def treats(people: int) -> int:
    """A function for treat eaters."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """A function for costs."""
    return 0.5 * (tea_count) + 0.75 * (treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
