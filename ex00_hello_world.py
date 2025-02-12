"""My first exercise in COMP110"""

__author__ = "730551362"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name?")))


def guess_secret(word: str, secret, str, idx: int = 0) -> bool:

    print(guess_secret(word=input("What is your word? "), secret=SECRET))
    print(guess_secret(word=input("What is your word? "), secret=SECRET, idx=2))
